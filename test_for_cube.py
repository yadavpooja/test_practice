def cube(n):
    return n ** 3


import unittest

class Mytest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(3),27)

unittest.main()
