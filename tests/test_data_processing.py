# tests/test_data_processing.py
import unittest
from app import get_clothing_recommendation

class TestDataProcessing(unittest.TestCase):
    def test_rain_clothing(self):
        self.assertEqual(get_clothing_recommendation(60, 'rainy'), "Bring an umbrella. A light jacket will do.")

    def test_cold_clothing(self):
        self.assertEqual(get_clothing_recommendation(40, 'clear'), "Wear a heavy jacket.")

    def test_warm_clothing(self):
        self.assertEqual(get_clothing_recommendation(80, 'sunny'), "It's warm enough for shorts and a t-shirt.")

if __name__ == '__main__':
    unittest.main()