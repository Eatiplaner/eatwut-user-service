import json
import secrets
import bcrypt
import re
from unidecode import unidecode

from app.constants.regex import passwordRegex

from mongoengine import BooleanField, \
    Document, EmailField, IntField, ListField, ReferenceField, StringField, \
    DoesNotExist, Q, signals

from .address import Address


class User(Document):
    ID = IntField(min_value=1)
    username = StringField(max_length=30, required=True, unique=True)
    full_name = StringField(max_length=30, required=True)
    password = StringField(required=True)
    email = EmailField(required=True, unique=True)
    bio = StringField(max_length=500)
    phone = StringField()
    birthday = StringField()
    is_kol = BooleanField()

    addresses = ListField(ReferenceField(Address))

    meta = {
        'indexes': ['username', 'email']
    }

    def verify_password(self, input):
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
    def valid_password(cls, password):
        return re.match(passwordRegex, password) and len(password) >= 8

    @classmethod
    def generate_username(cls, full_name):
        username_unidecode = unidecode(full_name)
        username_lower_underscore = username_unidecode.lower().replace(" ", "_")
        return username_lower_underscore

    @classmethod
    def generate_hash_password(cls, password):
        salt = bcrypt.gensalt()
        encode_passwd = password.encode("utf-8")

        return (bcrypt.hashpw(encode_passwd, salt)).decode("utf-8")

    @classmethod
    def pre_save_user(cls, sender, document, **kwargs):
        full_name = document.full_name
        username = User.generate_username(full_name)
        try:
            if User.objects.get(Q(full_name=full_name) | Q(username=username)):
                hashed = "_" + secrets.token_hex(3)
                document.username = username + hashed
        except DoesNotExist:
            document.username = username


signals.pre_save.connect(User.pre_save_user, sender=User)
