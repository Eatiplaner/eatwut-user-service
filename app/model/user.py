from mongoengine import BooleanField, \
    Document, EmailField, ListField, ReferenceField, StringField

from .address import Address
from app.constants.regex import passwordRegex


class User(Document):
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(min_length=8, required=True, regex=passwordRegex)
    first_name = StringField(max_length=10, required=True)
    last_name = StringField(max_length=10, required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField()
    birthday = StringField()
    is_kol = BooleanField()

    addresses = ListField(ReferenceField(Address))

    meta = {
        'indexes': ['username', 'email']
    }
