from enum import unique

from mongoengine import BooleanField, \
    Document, ListField, ReferenceField, StringField

from .address import Address


class User(Document):
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(min_length=8, required=True,
                           regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
                                 '(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    first_name = StringField(max_length=10, required=True)
    last_name = StringField(max_length=10, required=True)
    email = StringField(required=True, unique=True,
                        regex='[a-z0-9._%+!$&*=^|~#%{}/-]+@'
                              '([a-z0-9-]+.){1,}([a-z]{2,22})')
    phone = StringField()
    birthday = StringField()
    is_kol = BooleanField()

    addresses = ListField(ReferenceField(Address))

    meta = {
        'indexes': ['username']
    }
