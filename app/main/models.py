from mongoengine import Document, StringField, EmailField, IntField


class Donator(Document):
    nickname = StringField(required=False, max_length=100)
    email = EmailField(required=True)
    amount = IntField(required=True, min_value=0)

    meta = {
        'indexes': ['email']
    }

    def __repr__(self):
        return '<Donator %r>' % self.email