from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show
from bokeh.plotting import figure
import numpy as np
import random

from panels import project_tabs

curdoc().add_root(project_tabs)
show(project_tabs)

# - Gráfico de barras de leyes por años con la opcion de señalar partidos y/o ratio por cantidad del partido.
# - Gráfico de barras de cantidad de congresistas por partido por periodo. *
# - Gráfico de barras apiladas de Temas de Leyes por partido (o por candidato) por año.
# * Gráficos no seguros en el dashboard
