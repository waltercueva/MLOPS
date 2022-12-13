from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure

from models import database_config
from models.topic import Topic
from models.congress import Congress
from models.law import Law
db = database_config()

def get_topics():
    return [ t.name for t in db.query(Topic).all() ]

def get_parties():
    return [k for k in { c.part: 1 for c in db.query(Congress).all() }.keys()]

# 10 años

def get_laws():
    return [ l for l in db.query(Law).all() ]


def create_figure(height=300, width=500):
    topics = get_topics()
    laws = get_laws()
    topics_dict = {}
    temp_data = {}

    idx = 0
    for topic in topics:
        topics_dict[topic] = idx
        idx += 1
    for law in laws:
        parties = set()
        for congress in law.congress:
            parties.add(congress.party)
        for party in parties:
            if party not in temp_data:
                temp_data[party] = [0]*len(topics)
            for topic in law.topic:
                temp_data[party][topics_dict[topic.name]] += 1
    data = []
    for (k, v) in temp_data.items():
        data.append({
            'party': k,
            'laws': v
        })

    x = [(d['party'], topic) for d in data for topic in topics]

    nd = {}
    for i in range(len(topics)):
        nd[topics[i]] = []
        for d in data:
            nd[topics[i]].append(d['laws'][i])

    counts = sum(zip(*[nd[t] for t in topics]), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    fig = figure(x_range=FactorRange(*x), plot_height=height, plot_width=width,
                 title="Leyes por tema por partido político",
                 toolbar_location=None, tools="")
    fig.vbar(x='x', top='counts', width=0.9, source=source)
    return fig
