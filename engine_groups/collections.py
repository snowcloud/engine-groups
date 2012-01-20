# collections

from mongoengine import *
from depot.models import Location
from engine_groups.models import Membership

class Collection(Document):
    """
    An account can be held 
    
    """
    name = StringField(max_length=100, required=True)
    owner = ReferenceField('Account', required=True)
    tags = ListField(StringField(max_length=96), default=list)
    locations = ListField(ReferenceField(Location), default=list)
    members = ListField(ReferenceField(Membership), default=list)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.owner)
