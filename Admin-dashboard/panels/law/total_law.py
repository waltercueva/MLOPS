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

def get_laws():
    return [ l for l in db.query(Law).all() ]

def create_figure(height=300, width=500):
    laws = get_laws()
    data = {}
    for law in laws:
        law.date = datetime.strptime(law.date, '%Y-%m-%d %H:%M:%S')
        law.date = datetime(year=law.date.year, month=law.date.month, day=1)
        if law.date not in data:
            data[law.date] = 0
        data[law.date] += 1

    years = list(data.keys())
    counts = list(data.values())

    p = figure(x_range=[str(y)[:7] for y in years], plot_height=250, title="Conteo de leyes por Año",
               toolbar_location=None, tools="")
    p.vbar(x=[str(y)[:7] for y in years], top=counts, width=0.95)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p
