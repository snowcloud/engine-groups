from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from mongoengine.base import ValidationError
from mongoengine.queryset import OperationError, MultipleObjectsReturned, DoesNotExist
from pymongo.objectid import ObjectId

from engine_groups.models import Account

def get_one_or_404(**kwargs):
    try:
       object = Account.objects.get(**kwargs)
       return object
    except (MultipleObjectsReturned, ValidationError, DoesNotExist):
        raise Http404
    
def index(request):
    objects = Account.objects
    return render_to_response('engine_groups/index.html',
        RequestContext( request, { 'objects': objects }))
