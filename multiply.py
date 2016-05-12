def multiply(a,b):
    return a * b



import unittest
class Multiply(unittest.TestCase):

    def test_mul(self):
        self.assertEqual(multiply(4,2),8)
        self.assertEqual(multiply(1,0),0)
        self.assertEqual(multiply(3,3),9)
        self.assertEqual(multiply(1,-2),-2)



if __name__ == "__main__":
    unittest.main()
