import tldextract
from mongoengine import BooleanField, \
    Document, StringField, signals


class Provider(Document):
    # SCHEMA
    url = StringField(required=True, unique=True)
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
        match domain:
            case ('facebook' | 'instagram' | 'youtube' | 'tiktok') as type_url:
                document.type = type_url
            case _:
                document.type = ""


signals.pre_save.connect(Provider.pre_save, sender=Provider)
