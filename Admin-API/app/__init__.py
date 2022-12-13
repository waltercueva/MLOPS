from flask import Flask

from app.blueprints import blueprints_config
from app.models import database_config

app = Flask(__name__)
database_config(app)
blueprints_config(app)
