from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc, show

# import panels.congress as panel_congress
# import panels.law as panel_law
# import panels.topic as panel_topic
from .congress import tab as congress_tab
from .topic import tab as topic_tab
from .law import tab as law_tab

project_tabs = Tabs(tabs=[congress_tab, topic_tab, law_tab])
curdoc().add_root(project_tabs)



