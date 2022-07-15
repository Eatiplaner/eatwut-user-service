import json

import tldextract
from mongoengine import BooleanField, \
    Document, IntField, StringField, signals

from app.model.concerns.generatable_id import auto_increment_id

TYPEURLS = ['facebook', 'instagram', 'youtube', 'tiktok']


class Provider(Document):
    # SCHEMA
    ID = IntField(min_value=1, unique=True)
    url = StringField(required=True)
    type = StringField()
    display_on_profile = BooleanField(default=True)

    # INSTANCE METHODS
    def proto_data(self):
        data = json.loads(self.to_json())
        data['id'] = self.ID

        del data['_id']
        del data['ID']

        return data

    # CLASS METHODS

    # CALLBACKS
    @classmethod
    @auto_increment_id
    def pre_save(cls, sender, document, **kwargs):
        cls.generate_type_url(document)

    @classmethod
    def generate_type_url(cls, document):
        url_struct = tldextract.extract(document.url)
        domain = url_struct.domain
        if domain in TYPEURLS:
            document.type = domain
        else:
            document.type = "unknown"


signals.pre_save.connect(Provider.pre_save, sender=Provider)
