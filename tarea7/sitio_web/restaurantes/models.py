from django.db import models

from mongoengine import *

import datetime

connect('test')

class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()
    zipcode  = IntField()
    coord    = GeoPointField()

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField(min_value=1, unique=True)
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)
    grades           = ListField(EmbeddedDocumentField(likes))
    photo            = ImageField()
