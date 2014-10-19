
# flask import
from flask import render_template, request, jsonify
from flask.ext.babel import gettext as _

# project import
from app.utilis.decorators import title, ajax_view
from . import mod
from .forms import DonatorForm


@mod.route('/')
@title(_('Persian Libre Font Campaign'))
def index():
    return render_template('index.html', form=DonatorForm())


@mod.route('donate/', methods=['POST'])
@ajax_view
def donate():
    form = DonatorForm(request.form)

    if form.validate():
        return jsonify({'status': 1})
    return jsonify({'status': 2, 'form': render_template('donate_form.html', form=form)})