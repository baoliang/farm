#coding: utf-8
from service.account import vertify_user
from service.account import check_only_user
from service.account import reg_user
from service.info import create_info
from service.account import update_user
from service.city import get_city_by_id
from service.info import get_info_list
from lib.db import db, db_update
from lib.store import insert, find

import unittest

class Test_account(unittest.TestCase):


    
    def setUp(self):
        db_update.users.insert({
            '_id': 'test',
            'password': 'test', 
            'city':u'北京市'
        })
		 
    def tearDown(self):
        db_update.users.remove({'_id': 'test'}) 
        db_update.info.remove({'uid':'test'})
        db_update.test_info.remove()	 
		 
    def test_vertify_user(self):
        self.assertEqual(vertify_user('', '' ), False)
        self.assertTrue(bool(vertify_user('test', 'test')))
		 
		 
    def test_check_only_user(self):
        self.assertEqual(check_only_user('test'), False)
        self.assertEqual(check_only_user('test_false'), True)
		
		
    def test_reg_user(self):
        reg_user({'_id':'test'})
        self.assertTrue(bool(db.users.find_one({'_id':'test'})))

    def test_update_user(self):
        update_user('test', {'test':True})
        self.assertEqual(True, db.users.find_one({'_id': 'test'}).get('test'))
    

    
    def test_get_city_by_id(self):
        self.assertEqual(u'北京市', get_city_by_id('1')['name'])


class TestInfo(unittest.TestCase):

    create_info_data= {'test':'test'}	 
    def test_create_info(self):
        create_info('info_test', self.create_info_data, 'test')
        self.assertTrue(bool(db.info.find_one({'test':'test'})))

    def test_get_info_list(self):
        for i in range(100):
            self.create_info_data.pop('_id')
            insert('test_info', self.create_info_data)
        self.assertEqual(get_info_list('test_info', {}, 0, 0).count(), 100)

    
if __name__ == '__main__':
    unittest.main()
