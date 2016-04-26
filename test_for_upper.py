import unittest

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.foo = "hello world"

    def test_upper(self):
        self.assertEqual(self.foo.upper(),'HELLO WORLD')

    def test_isupper(self):
        self.assertTrue(self.foo.islower())
        self.assertFalse(self.foo.isupper())

    def test_split(self):
        self.assertEqual(self.foo.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            self.foo.split(2)


if __name__ == '__main__':
    unittest.main()
