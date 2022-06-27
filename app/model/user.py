from mongoengine import BooleanField, \
    Document, ListField, ReferenceField, StringField

from .address import Address


class User(Document):
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(required=True)
    first_name = StringField(max_length=10, required=True)
    last_name = StringField(max_length=10, required=True)
    email = StringField(required=True)
    phone = StringField()
    birthday = StringField()
    is_kol = BooleanField()

    addresses = ListField(ReferenceField(Address))

    meta = {
        'indexes': ['username']
    }
