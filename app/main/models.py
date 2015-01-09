# -*- coding: utf-8 -*-

# python import
from hashlib import md5
# from base64 import b64encode
from datetime import datetime
from mongoengine import Document, StringField, EmailField, IntField, DateTimeField, ReferenceField, BooleanField
# from urllib import urlencode

# flask import
# from flask import url_for


class Donator(Document):
    nickname = StringField(max_length=100)
    email = EmailField(required=True)
    donated = BooleanField(default=False)
    md5 = StringField(required=True)

    meta = {
        'indexes': ['email', 'donated']
    }

    @property
    def name(self):
        return self.nickname or self.email

    @property
    def avatar(self):
        # default images for gravatar can be 'wavatar' or 'monsterid'
        return "http://gravatar.com/avatar/{}?s=60&d=wavatar".format(self.md5)
        # return "http://rokh.chehrak.com/{}?{}".format(
        #     self.md5, urlencode({'size': 64,
        #                          'default': url_for('static', filename='image/avatar.png', _external=True),
        #                          'hash': b64encode(self.email)}))

    def save(self, *args, **kwargs):
        self.md5 = md5(self.email).hexdigest()
        super(Donator, self).save(*args, **kwargs)

    @property
    def donates(self):
        return int(Donate.objects(confirm=True, donator=self).sum('amount'))

    def __repr__(self):
        return '<Donator %r>' % self.email


class Donate(Document):
    amount = IntField(required=True, min_value=0)
    RefID = StringField()
    date = DateTimeField(required=True, default=datetime.now())
    donator = ReferenceField(Donator, required=True)
    confirm = BooleanField(required=True, default=False)

    meta = {
        'indexes': ['confirm']
    }

    def __repr__(self):
        if self.confirm:
            return '<Donated %r Rials - %r>' % (self.amount, self.date)
        return 'Donate %r' % self.amount
