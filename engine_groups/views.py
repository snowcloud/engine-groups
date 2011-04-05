from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from mongoengine.base import ValidationError
from mongoengine.queryset import OperationError, MultipleObjectsReturned, DoesNotExist
from pymongo.objectid import ObjectId

from engine_groups.models import Account
from forms import AccountForm

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

def detail(request, object_id, template_name='engine_groups/detail.html'):
    group = get_one_or_404(id=object_id)
    
    return render_to_response(
        template_name,
        {'object': group},
        RequestContext(request)
    )
    
@user_passes_test(lambda u: u.is_staff)
def edit(request, object_id, template_name='engine_groups/edit.html'):

    object = get_one_or_404(id=object_id)
    
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=object)
        if form.is_valid():
            g = form.save()
            print '**********'
            print g.name
            return HttpResponseRedirect(reverse('group', args=[object.id]))
    else:
        form = AccountForm(instance=object)
    
    template_context = {'form': form}

    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

@user_passes_test(lambda u: u.is_staff)
def new(request, template_name='engine_groups/edit.html'):
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            g = form.save()
            print '**********'
            print g.name
            return HttpResponseRedirect(reverse('group', args=[g.id]))
    else:
        form = AccountForm()
    
    template_context = {'form': form}

    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

