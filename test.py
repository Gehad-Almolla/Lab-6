import unittest

class Test_Power(unittest.TestCase):
    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.pow = Power()
    def test_add(self):
        # Test addition functionality
        result = self.pow.pow(3, 3)
        self.assertEqual(result, 9)
