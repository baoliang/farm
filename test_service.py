from service.account_service import vertify_user
from flaskext.testing import TestCase


class Test_account(TestCase):
     def test_vertify_user(self):
         self.assertEquire(vertify_user('', '' ), False)
