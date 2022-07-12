import tldextract
from mongoengine import BooleanField, \
    Document, StringField, signals

TYPEURLS = ['facebook', 'instagram', 'youtube', 'tiktok']


class Provider(Document):
    # SCHEMA
    url = StringField(required=True)
    type = StringField()
    display_on_profile = BooleanField(default=True)

    # CLASS METHODS

    # CALLBACKS
    @classmethod
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
