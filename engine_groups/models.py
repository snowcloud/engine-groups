import datetime

from django.db.models import permalink
from django.template.defaultfilters import slugify

from mongoengine import *
from mongoengine.django.auth import User

MEMBER_ROLE = 'member'
ADMIN_ROLE = 'admin'
MENTOR_ROLE = 'mentor'
STATUS_OK = 'ok'
STATUS_SUSPENDED = 'suspended'
STATUS_CLOSED = 'closed'

    
class Membership(EmbeddedDocument):
    member = ReferenceField('Account', required=True)
    role = StringField(max_length=20, required=True, default=MEMBER_ROLE)

    def __unicode__(self):
        return u'%s, %s' % (self.member.name, self.role)

class Account(Document):
    """
    An account can be held 
    
    """
    name = StringField(max_length=100, required=True)
    local_id = StringField(max_length=20) # for demo, links to local user id
    email = EmailField()
    url = URLField()
    description = StringField(max_length=20)
    permissions = ListField(StringField(max_length=20))
    api_key = StringField(max_length=64)
    api_password = StringField(max_length=64)
    members = ListField(EmbeddedDocumentField(Membership))
    status = StringField(max_length=12, default=STATUS_OK )
    
    meta = {
        'ordering': ['name']
    }
            

    # created_by = ReferenceField(User)
    # created_at = DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super(Group, self).save(*args, **kwargs)
    
    # @permalink
    # def get_absolute_url(self):
    #     return 'group_detail', (), {'id': self.id}
