import json
import unittest

import os

from application.src.launcher import app


class TestContacts(unittest.TestCase):
    """Choice List Test Class"""

    def setUp(self):
        self.client = app.test_client
        self.test_data_1 = {
            'name': 'Test1',
            'emailId': 'test1@t.com',
            'numbers': ['9090909090']
        }
        self.test_data_2 = {
            'name': 'Test2',
            'emailId': 'test2@t.com',
            'numbers': ['9090909090']
        }

    def test_contacts_creation(self):
        """Test Contacts creation (POST request)"""
        res = self.client().post('/contacts/', data=json.dumps(self.test_data_1))
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.test_data_1['name'], response_data['name'])
        self.assertEqual(self.test_data_1['emailId'], response_data['emailId'])

    def test_get_all_contacts(self):
        """Test Contacts GET all"""
        res = self.client().post('/contacts/', data=json.dumps(self.test_data_2))
        res = self.client().get('/contacts/')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertIn("contacts", response_data)

    def test_get_contacts_by_search(self):
        """Test Contacts GET call by search params"""
        res = self.client().post('/contacts/', data=json.dumps(self.test_data_2))
        res = self.client().get('/contacts/?search=test')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertIn("contacts", response_data)


if __name__ == '__main__':
    if os.getenv('ENVIRONMENT', "testing") != "testing":
        print "set ENVIRONMENT to testing"
    else:
        unittest.main()
