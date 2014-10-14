# from app import db
from mongoengine import EmbeddedDocument, Document, StringField, IntField, ListField, EmailField, ReferenceField, DateTimeField
from datetime import datetime
from hashlib import sha384
from flask import session


class Skill(EmbeddedDocument):
    title = StringField(required=True)
    level = IntField(required=False, min_value=0, max_value=100)


class Work(EmbeddedDocument):
    title = StringField(required=True)
    img = StringField(required=False)
    description = StringField(required=True)


class Social(EmbeddedDocument):
    username = StringField(required=True)
    type = IntField(required=True)


class Profile(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    nickname = StringField(required=False, max_length=100)
    _password = StringField(required=True)
    title = StringField(required=False)
    email = EmailField(required=True)
    number = ListField(StringField(required=True, max_length=12))
    address = StringField(required=True)
    website = StringField(required=True)

    socials = ListField(ReferenceField(Social))

    skills = ListField(ReferenceField(Skill))
    works = ListField(ReferenceField(Work))
    objective = StringField()

    date_modified = DateTimeField(default=datetime.now)

    meta = {
        'indexes': ['email']
    }

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

        try:
            self.password = kwargs['password']
        except KeyError:
            pass

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = sha384(password).hexdigest()

    @staticmethod
    def login(email, password):
        password = sha384(password).hexdigest()

        try:
            user = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return False

        if user.password == password:
            session['logged_in'] = user.id
            return True
        return False

    def __repr__(self):
        return '<Profile %r>' % self.email