import unittest
from flask import current_app
from Controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.app = Controller().app
        self.app.testing = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        self.app_context.pop()
    

    def test_app_exists(self):
        self.assertFalse(current_app is None)


    def test_get_all_questions(self):
        response = self.client.get('/getAllQuestions')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn('Items', response.json)
        self.assertIsInstance(response.json['Items'], list)
    

    def test_get_all_users(self):
        response = self.client.get('/getAllUsers')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn('Items', response.json)
        self.assertIsInstance(response.json['Items'], list)
    

    def test_get_top_10_users(self):
        response = self.client.get('/getTop10Users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn('Items', response.json)
        self.assertIsInstance(response.json['Items'], list)
    

    def test_add_user(self):
        response = self.client.post('/user', json={
            'name': 'Test User',
            'points': 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn('msg', response.json)
        self.assertEqual(response.json['msg'], 'Added successfully')


if __name__ == '__main__':
    unittest.main()