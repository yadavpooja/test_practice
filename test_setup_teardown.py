import unittest

class Testfixtures(unittest.TestCase):
    def setUp(self):
        print(" In setUp()")
        self.fixture = range(1,6)

    def test(self):
        print("In Test()")
        self.assertEqual(self.fixture,range(1,6),"test failed")

    def tearDown(self):
        print("In TearDown()")
        del self.fixture


if __name__ == "__main__":
    unittest.main()
