## Task - 1:
class Account:
    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def checkBalance(self):
        return self.balance
    

class SavingsAccount(Account):
    def __init__(self, name, account_no, rate):
        super().__init__(name, account_no)
        self.rate = rate

    def withdraw(self, amount):
        if (self.balance - amount >= 0):
            return super().withdraw(amount)
        else:
            print(f"You don't have enough balance!!!")

    def interest(self):
        self.balance += self.balance*self.rate
        return f"Your this year's interest {self.balance*self.rate} and the new balance is {self.balance}"
    

class FixedAccount(Account):
    def __init__(self,name, account_no, limit):
        super().__init__(name, account_no)
        self.limit = limit

    def withdraw(self, amount):
        if (self.balance - amount >= self.limit):
            return super().withdraw(amount)
        else:
            print(f"You will cross the limit!!!")


a_1 = SavingsAccount("hfid", 2342, .05)
a_1.deposit(50000)
a_1.withdraw(10000)
a_1.interest()
print(a_1.checkBalance())

a_2 = FixedAccount("vnafjb", 762492, 10000)
a_2.deposit(50000)
a_2.withdraw(10000)
a_2.withdraw(40000)
print(a_2.checkBalance())