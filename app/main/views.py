from flask import render_template
from flask.ext.babel import gettext as _
from app.utilis.decorators import title
from . import mod


@mod.route('/')
@title(_('Persian Libre Font Campaign'))
def index():
    return render_template('index.html')