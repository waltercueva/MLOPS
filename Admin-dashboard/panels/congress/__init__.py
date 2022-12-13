from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure
import numpy as np
import random


from panels.congress import congress_city
from panels.congress import congress_party

law_layout = layout([congress_city.create_figure(), congress_party.create_figure()])
tab = Panel(child=law_layout, title="Congresistas")

