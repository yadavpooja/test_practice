import unittest
from bank import Bank_account

class Mytest(unittest.TestCase):
    def setUp(self):
        self.foo = Bank_account()

    def test_deposit(self):
        self.assertEqual(self.foo.deposit(100),100)


    def test_withdraw(self):
        self.foo.deposit(100)
        self.assertEqual(self.foo.withdraw(50),50)


if __name__ == "__main__":
    unittest.main()
