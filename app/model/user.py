import json
import bcrypt
import re

from app.constants.regex import passwordRegex

from mongoengine import BooleanField, \
    Document, EmailField, IntField, ListField, ReferenceField, StringField

from .address import Address


class User(Document):
    ID = IntField(min_value=1)
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(required=True)
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

    def verifyPassword(self, input):
        encode_passwd = self.password.encode("utf-8")

        if bcrypt.hashpw(input.encode("utf-8"), encode_passwd) == encode_passwd:
            return True
        else:
            return False

    def proto_data(self):
        data = json.loads(self.to_json())
        data['id'] = self.ID

        del data['_id']
        del data['ID']
        del data['addresses']
        del data['password']

        return data

    @classmethod
    def validPassword(cls, password):
        return re.match(passwordRegex, password) and len(password) >= 8

    @classmethod
    def generateHashPassword(cls, password):
        salt = bcrypt.gensalt()
        encode_passwd = password.encode("utf-8")

        return (bcrypt.hashpw(encode_passwd, salt)).decode("utf-8")
