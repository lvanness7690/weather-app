# tests/test_app.py
import unittest
from app import app
from unittest.mock import patch

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_api_integration(self, mock_get):
        mock_data = {
            "main": {"temp": 75, "humidity": 65},
            "weather": [{"main": "Clear", "description": "clear sky"}],
            "wind": {"speed": 5},
            "sys": {"sunrise": 1588337844, "sunset": 1588387000},
            "coord": {"lat": 40.7128, "lon": -74.0060},
            "cod": 200
        }
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = self.client.post('/', data={'user_input': 'New York'})
        self.assertIn('75', response.data.decode())  # Check if temperature is in the response

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()