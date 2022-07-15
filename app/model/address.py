import json

from mongoengine import Document, IntField, StringField, signals


class Address(Document):
    ID = IntField(min_value=1, unique=True)
    district = StringField(required=True)
    city = StringField(required=True)
    lat = StringField()
    lng = StringField()
    type = StringField(required=True)

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

    @classmethod
    def generate_ID(cls, document):
        document.ID = Address.objects.count() + 1


signals.pre_save.connect(Address.pre_save, sender=Address)
