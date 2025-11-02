import unittest
from Power import Power
class TestPower(unittest.TestCase):
    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.pow = Power()
    def test_add(self):
        # Test addition functionality
        result = self.pow(3, 3)
        self.assertEqual(result, 9)
