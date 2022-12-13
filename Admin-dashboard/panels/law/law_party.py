from bokeh.plotting import figure
import numpy as np
import random
from models import database_config
from models.topic import Topic
from models.congress import Congress
from models.law import Law
from datetime import datetime
db = database_config()

def get_topics():
    return [ t.name for t in db.query(Topic).all() ]

def get_parties():
    return [k for k in { c.part: 1 for c in db.query(Congress).all() }.keys()]

# 10 años

def get_laws():
    return [ l for l in db.query(Law).all() ]

def create_figure(height=1000, width=1000):
    laws = get_laws()
    topics = get_topics()
    topics_dict = {}

    idx = 0
    for topic in topics:
        topics_dict[topic] = idx
        idx += 1

    temp_data = {}
    for law in laws:
        law.date = datetime.strptime(law.date, '%Y-%m-%d %H:%M:%S')
        law.date = datetime(year=law.date.year, month=law.date.month, day=1)

        parties = set()
        for congress in law.congress:
            parties.add(congress.party)

        for party in parties:
            if party not in temp_data:
                temp_data[party] = {}
            if law.date not in temp_data[party]:
                temp_data[party][law.date] = 0
            temp_data[party][law.date] += 1

    data = []
    for (k, v) in temp_data.items():
        data.append({
            'name': k,
            'data': [ itv for (itk, itv) in v.items() ],
            'dates': [ itk for (itk, itv) in v.items() ]
        })
    fig = figure(plot_width=width, plot_height=height, x_axis_type="datetime")
    for d in data:
        color = random.randint(1, 256 * 256 * 256)

        fig.line(d['dates'], d['data'],
                 color=(color % 256, int(color / 256 % 256), int(color / 256 / 256)),
                 legend=d['name'])

    fig.title.text = "Leyes por Partido en el tiempo"
    fig.legend.location = "top_left"
    fig.grid.grid_line_alpha = 0
    fig.xaxis.axis_label = 'Fecha'
    fig.yaxis.axis_label = 'Cantidad'
    fig.ygrid.band_fill_color = "olive"
    fig.ygrid.band_fill_alpha = 0.1
    return fig
