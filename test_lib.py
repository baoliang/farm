#coding: utf-8
import unittest
from random import randint
from datetime import datetime
from lib.store import insert, remove
from lib.store import find
from lib.page import get_page
from lib.utils import now
class Test_lib(unittest.TestCase):
    def setUp(self):
        '''
        @todo: 初始化测试
        '''
        for i in range(1000):
            insert(
                'test',
                {
                    'test_data': randint(1,10000)
                }
            )
        
    def tearDown(self):
        remove('test', real=True)
        
    def test_get_page(self):
        '''
        @todo: 测试分页
        '''
        resault = get_page('test', {'page':1}, limit=10) 
        self.assertEqual(resault['count'], 1000)
        self.assertEqual(resault['data'][9]['create_time'], resault['last_time'])
        self.assertEqual(len(resault['data']), 10)
        remove('test', real=True)
        resault = get_page('test', {'page':1}, limit=10) 
        self.assertEqual(resault['count'], 0)
        self.assertEqual(None, resault['last_time'])

        
if __name__ == '__main__':
    unittest.main()
