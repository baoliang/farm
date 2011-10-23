#coding: utf-8
from service.account import vertify_user
from service.account import check_only_user
from service.account import reg_user
from service.info import create_info
from service.account import update_user
from service.city import get_city_by_id
from lib.db import db, db_update

import unittest

class Test_account(unittest.TestCase):


    create_info_data= {'test':'test'}	 
    def setUp(self):
        db_update.users.insert({'_id': 'test', 'password': 'test'})
		 
    def tearDown(self):
        db_update.users.remove({'_id': 'test'}) 
        db_update.info.remove({'uid':'test'})
		 
		 
    def test_vertify_user(self):
        self.assertEqual(vertify_user('', '' ), False)
        self.assertEqual(vertify_user('test', 'test'), True)
		 
		 
    def test_check_only_user(self):
        self.assertEqual(check_only_user('test'), False)
        self.assertEqual(check_only_user('test_false'), True)
		
		
    def test_reg_user(self):
        reg_user({'_id':'test'})
        self.assertTrue(bool(db.users.find_one({'_id':'test'})))


    def test_create_info(self):
        create_info(self.create_info_data, 'test')
        self.assertTrue(bool(db.info.find_one({'uid':'test'})))


    def test_update_user(self):
        update_user('test', {'test':True})
        self.assertEqual(True, db.users.find_one({'_id': 'test'}).get('test'))
    

    
    def test_get_city_by_id(self):
        self.assertEqual(u'北京市', get_city_by_id('1')['name'])
if __name__ == '__main__':
    unittest.main()
