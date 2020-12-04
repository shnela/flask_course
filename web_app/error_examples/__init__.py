from flask import Blueprint

bp = Blueprint('error_examples', __name__)

from . import views  # views must be registered
