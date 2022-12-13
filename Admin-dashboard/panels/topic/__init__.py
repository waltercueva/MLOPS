from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure
import numpy as np
import random

from panels.topic import topic_time
from panels.topic import topic_party


topic_layout = layout([topic_time.create_figure(), topic_party.create_figure()])
tab = Panel(child=topic_layout, title="Temas de Leyes")

