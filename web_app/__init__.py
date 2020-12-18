import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from .config import Config

CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap5(app)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

from . import views  # views must be registered
