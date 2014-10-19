# -*- coding: utf-8 -*-

# python import
import mandrill
from datetime import datetime
from time import time

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
    try:
        mandrill_client = mandrill.Mandrill('jiOkNnvrJMuKEqD_hnRbTQ')
        message = {
            'html': '<p>Example HTML content</p>',
            'from_email': 'noreply@librefont.ir',
            'from_name': 'کمپین قلم فارسی آزاد',
            'subject': 'تشکر',
            'to': [{'email': 'hamidfzm@gmail.com',
                    'name': 'Hamid FzM',
                    'type': 'to'}],
            'google_analytics_domains': ['librefont.ir'],

        }

        result = mandrill_client.messages.send(message=message, async=True)
        print result
    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
        raise
    return jsonify({'status': 2, 'form': render_template('donate_form.html', form=form)})