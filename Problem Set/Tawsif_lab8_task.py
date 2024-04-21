"""
Develop a banking system where there is an “Account” class. This class will have an
attribute “balance” denoting the balance of the account. You can deposit some amount of
money in the account through a method called deposit(amount). You can also withdraw
an amount of money through a method called withdraw(amount). But if the user tries to
withdraw an amount more than their current balance, raise a custom error called
“NotEnoughBalance”. Inside the withdraw() function, raise this error when appropriate,
and also deal with this error using try and except blocks.
"""

"""
make logs
use datetime module to keep time data
use decorators for deposit and withdraw
use multiple decorators
"""

class NotEnoughBalance(Exception):
    """Raised when withdrawal amoount is greater than balance"""
    pass

    

class Account:
    def __init__(self):
        self.balance = 1000

    
    def log_balance(self, func):
        def wrapper():
            print(f"Previous Balance: {self.balance}")
            value = func(self.amount)
            print(f"Current Balance: {self.balance}")
            return value
        return wrapper
    
    
    @log_balance
    def deposite(self, amount):
        self.amount = amount
        self.balance += amount

    @log_balance
    def withdraw(self, amount):
        self.amount = amount
        try:
            if (self.balance < amount):
                raise NotEnoughBalance("Your withdrawal amount exceded current balance.")
        except NotEnoughBalance as neb:
            print(neb)
        else:
            self.balance -= amount



ac_1 = Account()
ac_1.deposite(50000)
print(ac_1.balance)
ac_1.withdraw(50000)
print(ac_1.balance)
ac_1.withdraw(2000)
print(ac_1.balance)
ac_1.withdraw(1000)
print(ac_1.balance)
