from .law import lawbp
from .congress import congressbp
from .topic import topicbp

def blueprints_config(app):
    app.register_blueprint(lawbp, url_prefix='/law')
    app.register_blueprint(congressbp, url_prefix='/congress')
    app.register_blueprint(topicbp, url_prefix='/topic')