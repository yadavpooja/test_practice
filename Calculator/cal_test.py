import unittest
from calculator import Calculator

class Mytest(unittest.TestCase):
    def setUp(self):
        self.foo = Calculator(3,2)

    def test_add(self):
        self.assertEqual(self.foo.add(), 5)

    def test_sub(self):
        self.assertEqual(self.foo.sub(),1)

    def test_mul(self):
        self.assertEqual(self.foo.mul(),6)

    def test_div(self):
        self.assertEqual(self.foo.div(), 1)

if __name__ == "__main__":
    unittest.main()



