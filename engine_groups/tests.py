# -*- coding: utf-8 -*-
"""
engine-groups/tests.py
"""

from django.test import TestCase, TransactionTestCase
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
# SEP = '**************'
# 
# def _print_db_info():
#     """docstring for _print_db_info"""
#     print SEP
#     print 'Resource: ', Resource.objects.count()
#     print 'Location: ', Location.objects.count()
#     print SEP
    
class AccountTest(TransactionTestCase):
    
    def test_account(self):
        print 'woooot'
