# -*- coding: utf-8 -*-

# python import
from mongoengine import ValidationError, DoesNotExist
from htmlmin.main import minify
from datetime import datetime
import traceback
from suds.client import Client

# flask import
from flask import render_template, request, jsonify, url_for, abort, current_app, redirect
from flask.ext.babel import gettext as _

# project import
from app.utilis.decorators import title, ajax_view
from app import mandrillemail
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
    try:
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

            cl = Client(current_app.config['ZARINPAL_WEBSERVICE'])
            result = cl.service.PaymentRequest(current_app.config['MMerchantID'],
                                               donate_obj.amount,
                                               'Donate from %s' % donator_obj.name,
                                               donator_obj.email,
                                               '',
                                               str(url_for('main.donate_callback', _external=True, donate_id=donate_obj.pk)))
            if result.Status == 100:
                # connect to bank here
                return jsonify({'status': 1, 'redirect': 'https://www.zarinpal.com/pg/StartPay/' + result.Authority})
            else:
                return jsonify({'status': 3, 'error': 'Error %d' % result.Status})

        return jsonify({'status': 2, 'form': minify(render_template('donate_form.html', form=form))})
    except Exception as e:
        traceback.print_exc()
        print e.message
        return abort(500)


@mod.route('donate/callback/<donate_id>/', methods=["GET", "POST"])
def donate_callback(donate_id):
    try:

        donate_obj = Donate.objects.get(id=donate_id)
        donator_obj = donate_obj.donator

        cl = Client(current_app.config['ZARINPAL_WEBSERVICE'])
        if request.args.get('Status') == 'OK':
            result = cl.service.PaymentVerification(current_app.config['MMerchantID'],
                                                    request.args['Authority'],
                                                    donate_obj.amount)
            if result.Status == 100:

                donate_obj.confirm = True
                donate_obj.RefID = result.RefID
                donate_obj.save()

                donator_obj.donated = True
                donator_obj.save()

                mandrillemail.send(_('Thanks'), donator_obj.email, donator_obj.nickname, render_template('email.html'))

                return redirect(url_for('main.thanks'))
            else:
                donate_obj.delete()
                if not donator_obj.donated:
                    donator_obj.delete()

                return jsonify({'status': 3, 'error': 'Error %d' % result.Status})
        else:
            # payment cancelled by user
            donate_obj.delete()
            if not donator_obj.donated:
                donator_obj.delete()

            return redirect(url_for('main.index'))

    except (ValidationError, DoesNotExist):
        return abort(404)

    except KeyError:
        return abort(403)

    except Exception as e:
        traceback.print_exc()
        print e.message
        return abort(500)


@mod.route('thanks/')
def thanks():
    return render_template('email.html')
