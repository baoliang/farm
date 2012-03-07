# _*_ coding: utf-8 _*_
from service.account import vertify_user
from service.account import check_only_user
from service.account import reg_user
from service.info import create_info
from service.account import update_user
from service.city import get_city_by_id
from service.info import get_info_list
from service.info import del_info
from service.info import update_info
from lib.db import db, db_update
from lib.store import insert, find, find_one, remove

import unittest

class Test_account(unittest.TestCase):    
    def setUp(self):
        insert("users",
            { "_id" : "test", "province" : "北京市", "city" : "东城区", "area_id" : "", "password" : "admin", "name" : "admin", "city_id" : "39", "st_code" : 0, "leval" : "1", "create_time" : "2012-03-07 16:55:17.360058", "province_id" : "1" })
		 
    def tearDown(self):
        db_update.users.remove({'_id': 'test'}) 
        db_update.info.remove({'uid':'test'})
        db_update.test_info.remove()	 
		 
    def test_vertify_user(self):
        self.assertEqual(vertify_user('', '' ), False)
        self.assertTrue(bool(vertify_user('test', 'admin')))
		 
		 
    def test_check_only_user(self):
        self.assertEqual(check_only_user('test'), False)
        self.assertEqual(check_only_user('test_false'), True)
		
		
    def test_reg_user(self):
        reg_user({'_id':'test_reg'})
        self.assertTrue(bool(find_one('users', {'_id':'test_reg'})))

    def test_update_user(self):
        update_user('test', {'test':True})
        self.assertEqual(True, db.users.find_one({'_id': 'test'}).get('test'))
    

    
    def test_get_city_by_id(self):
        self.assertEqual(u'北京市', get_city_by_id('1')['city_name'])


class TestInfo(unittest.TestCase):

    create_info_data= {'test':'test'}	 


    def setUp(self):
        insert(
            'users',
            { "_id" : "test_update", "province" : "北京市", "city" : "东城区", "area_id" : "", "password" : "admin", "name" : "admin", "city_id" : "39", "st_code" : 0, "leval" : "1", "create_time" : "2012-03-07 16:55:17.360058", "province_id" : "1" }
        )
    def tearDown(self):
        remove('users', {'_id': 'test_update'}, real=True)

    def test_create_info(self):
        create_info('info_test', self.create_info_data, 'test')
        self.assertTrue(bool(db.info_test.find_one({'test':'test'})))

    def test_get_info_list(self):
        for i in range(100):
            self.create_info_data.pop('_id')
            insert('test_info', self.create_info_data)
        self.assertEqual(get_info_list('test_info', {})['count'], 100)


    def test_del_info(self):
        del_info('users', {'_id': 'test_del'}, real=True)
        self.assertEqual(0, find('users',{'_id': 'test_del'}, return_type="cusor").count())
    

    def test_update_info(self):
        update_info('users', {'_id': 'test_update'},  {'city': 'hongkong'})
        self.assertEqual(
            'hongkong',
            find_one('users', {'_id': 'test_update'}).get('city', '')
        )

if __name__ == '__main__':
    unittest.main()
