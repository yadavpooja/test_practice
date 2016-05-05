def cube(n):
    return n ** 3


import unittest

class Mytest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(3),27)
        self.assertEqual(cube(2),8)
        self.assertEqual(cube(-1),-1)
        self.assertEqual(cube(0),0)
unittest.main()

