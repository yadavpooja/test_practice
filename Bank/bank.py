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
        if self.balance < self.min_bal:
            print "sorry low bal"
        else:
            Bank_account.withdraw(self,amount)


a = Bank_account()
#b = Minimum_bal(500)
#print b.withdraw(100)
#print a.withdraw(100) 
#a = Minimum_bal(200)
print a.deposit(100)
print a.withdraw(40)

