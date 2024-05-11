import unittest
from flask import url_for
from app import app

class TestFlaskRoutes(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_route(self):
        # Testing the index route
        response = self.app.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_convert_route(self):
        # Testing the convert route to see if works/returns values
        response = self.app.post(url_for('convert'), data=dict(amount='100', from_currency='CAD', to_currency='AUD'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
