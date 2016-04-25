class Bank_account():
    def __init__(self):
        self.balance = 0


    def deposit(self,amount):
        self.balance += amount
        return self.balance


    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

class Minimum_bal(Bank_account):
    def __init__(self,min_bal):
        Bank_account.__init__(self)
        self.min_bal = min_bal


    def withdraw(self,amount):
        if self.balance <= self.min_bal:
            return "sorry low bal"
        else:
            return Bank_account.withdraw(self,amount)


b = Minimum_bal(100)
print b.withdraw(50)
