from mongoengine import Document, StringField, EmailField, IntField, DateTimeField, ListField, EmbeddedDocument
from datetime import datetime


class Donate(Document):
    amount = IntField(required=True, min_value=0)
    date = DateTimeField(required=True, default=datetime.now())


class Donator(Document):
    nickname = StringField(required=False, max_length=100)
    email = EmailField(required=True)
    donate = ListField(EmbeddedDocument(Donate))

    meta = {
        'indexes': ['email']
    }

    def __repr__(self):
        return '<Donator %r>' % self.email