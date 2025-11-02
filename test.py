import unittest
from Power import Power   # import it!

class Test_Power(unittest.TestCase):
    def setUp(self):
        self.pow = Power()

    def test_add(self):
        result = self.pow.pow(3, 3)
        self.assertEqual(result, 9)

if __name__ == "__main__":
    unittest.main()
