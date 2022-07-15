import json

import tldextract
from mongoengine import BooleanField, \
    Document, IntField, StringField, signals

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
    def pre_save(cls, sender, document, **kwargs):
        cls.generate_ID(document)
        cls.generate_type_url(document)

    @classmethod
    def generate_type_url(cls, document):
        url_struct = tldextract.extract(document.url)
        domain = url_struct.domain
        if domain in TYPEURLS:
            document.type = domain
        else:
            document.type = "unknown"

    @classmethod
    def generate_ID(cls, document):
        document.ID = Provider.objects.count() + 1


signals.pre_save.connect(Provider.pre_save, sender=Provider)
