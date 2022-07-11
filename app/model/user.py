import json
import secrets
import bcrypt
import re

from unidecode import unidecode

from app.constants.regex import passwordRegex

from mongoengine import BooleanField, \
    Document, EmailField, IntField, ListField, ReferenceField, StringField, \
    DoesNotExist, signals

from .address import Address
from .provider import Provider


class User(Document):
    # SCHEMA
    ID = IntField(min_value=1, unique=True)
    username = StringField(max_length=30, required=True, unique=True)
    full_name = StringField(max_length=30, required=True)
    password = StringField(required=True)
    email = EmailField(required=True, unique=True)
    bio = StringField(max_length=500)
    phone = StringField()
    birthday = StringField()
    is_kol = BooleanField()

    addresses = ListField(ReferenceField(Address))
    providers = ListField(ReferenceField(Provider))

    meta = {
        'indexes': ['username', 'email']
    }

    # INSTANCE METHODS
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

    # CLASS METHODS
    @classmethod
    def valid_password(cls, password):
        return bool(re.match(passwordRegex, password)) and len(password) >= 8

    # CALLBACKS
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        cls.generate_ID(document)
        cls.generate_username(document)
        cls.generate_hash_password(document)

    @classmethod
    def generate_hash_password(cls, document):
        salt = bcrypt.gensalt()
        encode_passwd = document.password.encode("utf-8")

        document.password = bcrypt.hashpw(encode_passwd, salt).decode("utf-8")

    @classmethod
    def generate_username(cls, document):
        fullname_unidecode = unidecode(document.full_name)
        original_username = fullname_unidecode.lower().replace(" ", "_")
        username = original_username

        try:
            while (True):
                User.objects.get(username=username)
                username = f'{original_username}_{secrets.token_hex(3)}'
        except DoesNotExist:
            document.username = username

    @classmethod
    def generate_ID(cls, document):
        document.ID = User.objects.count() + 1


signals.pre_save.connect(User.pre_save, sender=User)
