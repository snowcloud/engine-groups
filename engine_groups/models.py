import datetime

from django.db.models import permalink
from django.template.defaultfilters import slugify

from mongoengine import *
from mongoengine.django.auth import User

MEMBER_ROLE = 'member'
ADMIN_ROLE = 'admin'
MENTOR_ROLE = 'mentor'

# mongoengine.django.auth.User

# class User(Document):
#     """A User document that aims to mirror most of the API specified by Django
#     at http://docs.djangoproject.com/en/dev/topics/auth/#users
#     """
#     username = StringField(max_length=30, required=True)
#     first_name = StringField(max_length=30)
#     last_name = StringField(max_length=30)
#     email = StringField()
#     password = StringField(max_length=128)
#     is_staff = BooleanField(default=False)
#     is_active = BooleanField(default=True)
#     is_superuser = BooleanField(default=False)
#     last_login = DateTimeField(default=datetime.datetime.now)
#     date_joined = DateTimeField(default=datetime.datetime.now)

class Membership(EmbeddedDocument):
    user = ReferenceField(Account)
    role = StringField(max_length=30, required=True, default=MEMBER_ROLE)
    
class Account(Document):
    title = StringField(max_length=100, required=True)
    slug = StringField(max_length=100, required=False, unique=True)
    members = ListField(EmbeddedDocumentField(GroupMembership))
    
    # resources = ListField(ReferenceField(Resource))
    # users = ListField(ReferenceField(User))
    # emails = ListField(EmailField())

    created_by = ReferenceField(User)
    created_at = DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Group, self).save(*args, **kwargs)
    
    @permalink
    def get_absolute_url(self):
        return 'group_detail', (), {'group_slug': self.slug}
