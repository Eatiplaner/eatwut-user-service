from mongoengine import Document, StringField


class Address(Document):
    district = StringField(required=True)
    city = StringField(required=True)
    lat = StringField()
    lng = StringField()
    type = StringField(required=True)
