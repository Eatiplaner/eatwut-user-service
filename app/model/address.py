import json

from mongoengine import Document, IntField, StringField, signals

from app.model.concerns.generatable_id import auto_increment_id


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
    @auto_increment_id
    def pre_save(cls, sender, document, **kwargs):
        return None


signals.pre_save.connect(Address.pre_save, sender=Address)
