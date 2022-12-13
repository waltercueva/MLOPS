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
# data = [{
#     "name": "Rojo",
#     "data": [3, 8, 4, 6],
#     "dates": ['1995', '1996', '1997', '1998']
# }, {
#     "name": "Verde",
#     "data": [1, 8, 10, 5],
#     "dates": ['1995', '1996', '1997', '1998']
# }]
#

def create_figure(height=300, width=500):
    laws = get_laws()
    topics = get_topics()
    topics_dict = {}

    idx = 0
    for topic in topics:
        topics_dict[topic] = idx
        idx += 1

    temp_data = {}
    for law in laws:
        law.date = datetime.strptime(law.date, '%Y-%m-%d %H:%M:%S').year
        for topic in law.topic:
            if topic.name not in temp_data:
                temp_data[topic.name] = {}
            if law.date not in temp_data[topic.name]:
                temp_data[topic.name][law.date] = 0
            temp_data[topic.name][law.date] += 1
    data = []
    for (k, v) in temp_data.items():
        data.append({
            'name': k,
            'data': [ itv for (itk, itv) in v.items() ],
            'dates': [ itk for (itk, itv) in v.items() ]
        })
    print(data)
    fig = figure(plot_width=width, plot_height=height, x_axis_type="datetime")
    for d in data:
        color = random.randint(1, 256 * 256 * 256)

        fig.line(d['dates'], d['data'],
                 color=(color % 256, int(color / 256 % 256), int(color / 256 / 256)),
                 legend=d['name'])

    fig.title.text = "Temas de Leyes en el tiempo"
    fig.legend.location = "top_left"
    fig.grid.grid_line_alpha = 0
    fig.xaxis.axis_label = 'Fecha'
    fig.yaxis.axis_label = 'Cantidad'
    fig.ygrid.band_fill_color = "olive"
    fig.ygrid.band_fill_alpha = 0.1
    return fig
