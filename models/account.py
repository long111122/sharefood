from mongoengine import *

class Account(Document):
    username = StringField()
    password = StringField()