# -*- coding: utf-8 -*-
"""
engine-groups/tests.py
"""

import os

from django.contrib.auth.models import User
from mongoengine.connection import _get_db as get_db
from mongoengine.django.tests import MongoTestCase

from depot.models import Resource
from engine_groups.models import Account, Membership, MEMBER_ROLE, ADMIN_ROLE
from engine_groups.collections import Collection

SEP = '**************'

# import json
# from mongoengine import base as mongobase
# from pymongo import json_util

def _dump_collections(collection_names=None):
    if collection_names is None:
        collection_names = [coll for coll in get_db().collection_names() if coll != 'system.indexes']
    for coll in collection_names:
        os.system('mongoexport -d {0} -c {1} -o output_{1}.json'.format(get_db().name, coll))

def _load_collections(collection_names=None, drop='--drop'):
    if collection_names is None:
        collection_names = [coll for coll in get_db().collection_names() if coll != 'system.indexes']
    for coll in collection_names:
        os.system('mongoimport -d {0} -c {1} --file output_{1}.json {2}'.format(get_db().name, coll, drop))

def _print_db_info():
    """docstring for _print_db_info"""
    print SEP
    print 'Account: ', Account.objects.count()
    print 'Membership: ', Membership.objects.count()
    print SEP

def _make_user(name):
    return User.objects.create_user(name, email="%s@example.com" % name, password='password')

class AccountsBaseTest(MongoTestCase):
    def setUp(self):
        # _print_db_info()
        self.user_humph = _make_user('bob')
        self.user_jorph = _make_user('jorph')
        self.user_group = _make_user('group')

        self.humph = Account.objects.create(name="Humph Floogerwhippel", email="humph@example.com", local_id=str(self.user_humph.id))
        self.jorph = Account.objects.create(name="Jorph Wheedjilli", email="jorph@example.com", local_id=str(self.user_jorph.id))
        self.group = Account.objects.create(
            name="Flupping Baxters of Falkirk", 
            email="group@example.com", 
            local_id=str(self.user_group.id),
            )
        self.group.add_member(self.humph)
        self.group.add_member(self.jorph, role=ADMIN_ROLE)

    def tearDown(self):
        # _print_db_info()
        pass
        
        # _dump_accounts('blah.json')
        # print 'dropping Account docs'
        # Account.drop_collection()
        # Membership.drop_collection()

class CollectionsTest(AccountsBaseTest):

    def test_creation(self):

        res1 = Resource.objects.create(
            title='blah', 
            tags=['blue', 'red'],
            author=self.humph
            )
        res2 = Resource.objects.create(
            title='blah 2', 
            tags=['green', 'red'],
            author=self.humph
            )
        res3 = Resource.objects.create(
            title='blah 3', 
            tags=['green', 'red'],
            author=self.jorph
            )
            
        c = Collection.objects.create(name='Test Collection', owner=self.humph)
        print 'collection', c

class AccountsTest(AccountsBaseTest):
    def test_account(self):

        # print self.group
        # print [m for m in self.group.members]
        self.assertEqual(Account.objects.count(), 3)
        _dump_collections()

    def test_load_accounts(self):
        
        """docstring for test_load_accounts"""
        _load_collections()
        self.assertEqual(Account.objects.count(), 3)
        # group = Account.objects.get(name='Flupping Baxters of Falkirk')
        arthur = _make_user('arthur')
        acct1 = Account.objects.create(name="Arthur Sixpence", email="arthur@example.com", local_id=str(arthur.id))
        # print acct.name
        self.group.add_member(acct1)
        self.group.save()
        self.assertEqual(len(self.group.members), 3)

        print self.group
        print [m for m in self.group.members]
        
        
        
        