import unittest

class Assertion_truth(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False,"test failed")

if __name__ == "__main__":
    unittest.main()
