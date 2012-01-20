# collections

from mongoengine import *


class Collection(Document):
    """
    An account can be held 
    
    """
    name = StringField(max_length=100, required=True)
