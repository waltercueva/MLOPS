from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure
import numpy as np
import random


from panels.law import law_party
from panels.law import total_law

law_layout = layout([law_party.create_figure(), total_law.create_figure()])
tab = Panel(child=law_layout, title="Leyes")

