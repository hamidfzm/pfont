__author__ = 'Hamid FzM'

from flask import Blueprint

mod = Blueprint('api', __name__, url_prefix='/api')

from . import views
