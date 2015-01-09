from flask import Blueprint

mod = Blueprint('main', __name__, url_prefix='/')

from . import views
