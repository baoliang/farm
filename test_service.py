#coding: utf-8
from service.account_service import vertify_user
from service.account_service import check_only_user
from service.account_service import reg_user
from lib.db import db, db_update
import unittest

class Test_account(unittest.TestCase):


    def setUp(self):
        db_update.users.insert({'_id': 'test', 'pass': 'test'})
		 
		 
    def tearDown(self):
        db_update.users.remove({'_id': 'test'}) 
		 
		 
    def test_vertify_user(self):
        self.assertEqual(vertify_user('', '' ), False)
        self.assertEqual(vertify_user('test', 'test'), True)
		 
		 
    def test_check_only_user(self):
        self.assertEqual(check_only_user('test'), False)
        self.assertEqual(check_only_user('test_false'), True)
		
		
	def test_reg_user(self):
        reg_user({''})
		
if __name__ == '__main__':
    unittest.main()
