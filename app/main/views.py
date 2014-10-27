# -*- coding: utf-8 -*-

# python import
from mongoengine import ValidationError, DoesNotExist
from htmlmin.main import minify
from datetime import datetime
import traceback

# flask import
from flask import render_template, request, jsonify, url_for, abort, current_app
from flask.ext.babel import gettext as _

# project import
from app.utilis.decorators import title, ajax_view
from . import mod
from .forms import DonatorForm
from .models import Donate, Donator


@mod.route('/')
@title(_('Persian Libre Font Campaign'))
def index():
    donator_obj = Donator.objects(donated=True)

    return render_template('index.html',
                           form=DonatorForm(),
                           donatores=donator_obj,
                           donators_count=len(donator_obj),
                           days_passed=(datetime.now() - current_app.config['CAMPAIGN_START']).days,
                           donates=int(Donate.objects(confirm=True).sum('amount')))


@mod.route('donate/', methods=['POST'])
@ajax_view
def donate():
    form = DonatorForm(request.form)

    if form.validate():
        # temporary naughty way

        try:
            donator_obj = Donator.objects.get(email=form.email.data.lower())

        except (ValidationError, DoesNotExist):
            donator_obj = Donator(email=form.email.data.lower(), nickname=form.nickname.data)

        donator_obj.commit()

        donate_obj = Donate(amount=form.amount.data, donator=donator_obj)
        donate_obj.save()

        # connect to bank here
        return jsonify({'status': 1, 'redirect': str(url_for('main.donate_callback', _external=True, donate_id=donate_obj.pk))})
    return jsonify({'status': 2, 'form': minify(render_template('donate_form.html', form=form))})


@mod.route('donate/callback/<donate_id>/', methods=["GET", "POST"])
def donate_callback(donate_id):
    try:
        # validate amount in here
        # request.args['au']

        donate_obj = Donate.objects.get(id=donate_id)
        donate_obj.confirm = True
        donate_obj.save()

        donator_obj = donate_obj.donator
        donator_obj.donated = True
        donator_obj.save()

        # print mandrillemail.send(_('Thanks'), donator_obj.email, donator_obj.nickname, 'Thanks for donating to librefont.')
        return 'Thank'

    except (ValidationError, DoesNotExist):
        return abort(404)

    except Exception as e:
        traceback.print_exc()
        print e.message
        return abort(500)

@mod.route('test')
def test():
    return render_template('email.html')