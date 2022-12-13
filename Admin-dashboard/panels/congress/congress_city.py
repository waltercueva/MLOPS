from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure

from datetime import datetime
from models import database_config
from models.topic import Topic
from models.congress import Congress
from models.law import Law
db = database_config()


def get_topics():
    return [ t.name for t in db.query(Topic).all() ]

def get_parties():
    return [k for k in { c.part: 1 for c in db.query(Congress).all() }.keys()]

def get_congress():
    return [c for c in db.query(Congress).all()]

def get_laws():
    return [ l for l in db.query(Law).all() ]

def create_figure(height=300, width=500):
    congress = get_congress()

    data = {}
    for c in congress:
        if not c.province:
            c.province = 'Desconocido'
        if c.province not in data:
            data[c.province] = 0
        data[c.province] += 1

    provinces = list(data.keys())
    counts = list(data.values())

    p = figure(x_range=[y for y in provinces], plot_height=250, title="Conteo de congresistas por Ciudad",
               toolbar_location=None, tools="")
    p.vbar(x=[str(y) for y in provinces], top=counts, width=0.95)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p
