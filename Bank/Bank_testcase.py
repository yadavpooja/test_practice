import unittest
from bank import Bank_account
from bank import Minimum_bal

class Mytest(unittest.TestCase):
    def setUp(self):
        self.foo = Bank_account()
        self.bal = Minimum_bal(1000)

    def test_deposit(self):
        self.assertEqual(self.foo.deposit(100),100)


    def test_withdraw(self):
        self.foo.deposit(100)
        self.assertEqual(self.foo.withdraw(50),50)

    def test_minbal(self):
        self.bal.balance = 2000
        self.assertEqual(self.bal.withdraw(1000),1000)
        self.assertEqual(self.bal.withdraw(100),"sorry low bal")


if __name__ == "__main__":
    unittest.main()
