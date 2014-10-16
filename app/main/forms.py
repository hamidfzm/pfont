# flask import
from flask.ext.wtf import Form
from wtforms import StringField, validators
from flask.ext.babel import gettext as _


class DonatorForm(Form):
    email = StringField(_('Email'), [
        validators.Length(min=6, max=100, message=_('Invalid email length')),
        validators.DataRequired(message=_('Field required')),
        validators.Email(message=_('Invalid email address')),
    ])

    nickname = StringField(_('Nickname'), [
        validators.Optional(),
        validators.Length(min=3, max=80, message=_('Invalid nickname'))
    ])

    amount = StringField(_('Amount'), [
        validators.DataRequired(message=_('Field required')),
        validators.Regexp(regex='^[1-9][0-9]{3,}$')
    ])