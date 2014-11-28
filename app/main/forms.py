# -*- coding: utf-8 -*-

# flask import
from flask.ext.wtf import Form
from wtforms import StringField, validators
# from flask.ext.babel import gettext as _


class DonatorForm(Form):
    email = StringField('Email', [
        validators.Length(min=6, max=100, message=u'طول پست الکترونیک باید بین ۶ تا ۱۰۰ کارکتر باشد'),
        validators.DataRequired(message=u'این قسمت اجباری است'),
        validators.Email(message=u'نشانی پست الکترونیک اشتباه است'),
    ])

    nickname = StringField('Nickname', [
        validators.Optional(),
        validators.Length(min=3, max=80, message=u'طول نام پرداخت‌کننده باید بین ۳ تا ۸۰ کارکتر باشد')
    ])

    amount = StringField('Amount', [
        validators.DataRequired(message=u'این قسمت اجباری است و از اعداد انگلیسی استفاده کنید.'),
        validators.Regexp(regex='^[1-9][0-9]{3,}$', message=u'حداقل مبلغ پرداختی ۱۰۰۰ تومان است.')
    ])
