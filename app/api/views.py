__author__ = 'Hamid FzM'

# python import
from datetime import datetime

# flask import
from flask import jsonify, current_app

# project import
from . import mod
from app.main.models import Donate, Donator


@mod.route('/v1/statistics/')
def statistics():
    donator_obj = Donator.objects(donated=True)
    donates = int(Donate.objects(confirm=True).sum('amount'))

    return jsonify(donators_count=donator_obj.count(),
                   days_passed=(datetime.now() - current_app.config['CAMPAIGN_START']).days,
                   percent=round((float(donates) / 10000000) * 100, 1),
                   donates=donates)
