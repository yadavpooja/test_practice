import unittest

class Equality(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1,3-2)

    def test_notequal(self):
        self.assertNotEqual(2,4-1)

if __name__ == '__main__':
    unittest.main()
