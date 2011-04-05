# -*- coding: utf-8 -*-
"""
engine-groups/tests.py
"""

from django.test import TestCase, TransactionTestCase
from engine_groups.models import Account, Membership, MEMBER_ROLE, ADMIN_ROLE

# # from firebox.ordnancesurvey import get_os_postcode, \
# #     OS_LABEL, OS_TYPE, OS_LAT, OS_LON, OS_WARD, OS_DISTRICT, OS_COUNTRY
# from firebox.views import *
# 
# from depot.models import Resource, Location, load_resource_data, \
#     get_place_for_postcode, lat_lon_to_str, get_location_for_postcode
# from depot.forms import ShortResourceForm
# from mongoengine import connect
# from mongoengine.connection import _get_db as get_db
# 
# TEST_DB_NAME = 'test_db2'
# 
# # TEST_URL = "http://www.gilmerton.btik.com/p_Pilates.ikml"
# TEST_URL = "http://www.gilmerton.btik.com/"
# TEST_URL_RESULT = 3
# TEST_URL2 = "http://www.anguscardiacgroup.co.uk/Programme.htm"
# TEST_URL2_RESULT = 20
# 
SEP = '**************'

import json
from mongoengine import base as mongobase
from pymongo import json_util

def _dump_accounts(fname):
    datas = []
    for u in Account.objects.all():
       datas.append(u.to_mongo())
    data = json.dumps(datas, sort_keys=True, indent=4, default=json_util.default) # Write to file.
    o = open(fname, 'w')
    o.write(data)
    o.close()

def _load_accounts(fname):
    """docstring for _load_accounts"""
    f = open(fname, 'r') # JSON file
    datas = json.loads(f.read(), object_hook=json_util.object_hook )
    for data in datas:
        model = mongobase._document_registry[data['_cls']]
        model_instance = model._from_son(data)
        model_instance.save(validate = False) # Ingore Ref fields

def _print_db_info():
    """docstring for _print_db_info"""
    print SEP
    print 'Account: ', Account.objects.count()
    # print 'Membership: ', Membership.objects.count()
    print SEP
    
class AccountTest(TransactionTestCase):
    def setUp(self):
        _print_db_info()

    def tearDown(self):
        _print_db_info()
        
        # _dump_accounts('blah.json')
        print 'dropping Account docs'
        Account.drop_collection()
        # Membership.drop_collection()
    
    def test_account(self):
        acct1 = Account(name='Humph Floogerwhippel')
        acct1.save()
        acct2 = Account(name='Jorph Wheedjilli')
        acct2.save()
        # print acct.name
        group = Account(name='Flupping Baxters of Falkirk', 
            members=[Membership(member=acct1), Membership(member=acct2, role=ADMIN_ROLE)])
        group.save()
        print group
        print [m for m in group.members]
        self.assertEqual(Account.objects.count(), 3)
        _dump_accounts('blah.json')

    def test_load_accounts(self):
        
        """docstring for test_load_accounts"""
        _load_accounts('blah.json')
        self.assertEqual(Account.objects.count(), 3)
        group = Account.objects.get(name='Flupping Baxters of Falkirk')
        acct1 = Account(name='Arthur Sixpence')
        acct1.save()
        # print acct.name
        group.members.append(Membership(member=acct1))
        group.save()
        self.assertEqual(len(group.members), 3)

        print group
        print [m for m in group.members]
        
        
        
        