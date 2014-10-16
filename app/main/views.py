
# flask import
from flask import render_template
from flask.ext.babel import gettext as _

# project import
from app.utilis.decorators import title
from . import mod
from .forms import DonatorForm


@mod.route('/')
@title(_('Persian Libre Font Campaign'))
def index():
    return render_template('index.html', form=DonatorForm())