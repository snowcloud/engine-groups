from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Example:
    
    url(r'^$', 'engine_groups.views.index', name='groups'),
    url(r'^new/$', 'engine_groups.views.new', name='group-new'),
    url(r'^(?P<object_id>\w+)/$', 'engine_groups.views.detail', name='group'),
    url(r'^(?P<object_id>\w+)/edit/$', 'engine_groups.views.edit', name='group-edit'),

    )