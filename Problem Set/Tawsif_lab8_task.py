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



from functools import wraps
import datetime

class NotEnoughBalance(Exception):
    """Raised when withdrawal amoount is greater than balance"""
    pass

    

class Account:
    def __init__(self):
        self.balance = 1000

    
    def log_balance(func):

        @wraps(func)
        def wrapper(self, amount):
            print(f"\n{datetime.datetime.now()}:\nAttempting {func.__name__} of {amount} BDT")
            value = func(self, amount)
            print(f"Current Balance: {self.balance}")
            return value
        return wrapper
    
    
    @log_balance
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount

    @log_balance
    def withdraw(self, amount):
        self.amount = amount
        try:
            if (self.balance < amount):
                raise NotEnoughBalance("Transaction Stopped!!! \nYour withdrawal amount exceded current balance.")
        except NotEnoughBalance as neb:
            print(neb)
        else:
            self.balance -= amount












# import datetime

# class NotEnoughBalance(Exception):
#     """Raised when withdrawal amount is greater than balance."""
#     pass

# class Account:
#     def __init__(self, initial_balance=1000):
#         self.balance = initial_balance

#     def log(func):
#         def wrapper(self, amount):
#             print(f"{datetime.datetime.now()}: Attempting {func.__name__} of {amount}")
#             result = func(self, amount)
#             print(f"{datetime.datetime.now()}: New Balance: {self.balance}")
#             return result
#         return wrapper

#     @log
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     @log
#     def withdraw(self, amount):
#         if self.balance < amount:
#             raise NotEnoughBalance("Your withdrawal amount exceeds current balance.")
#         self.balance -= amount
#         return self.balance

# # Example usage:
# ac_1 = Account()
# print(ac_1.deposit(50000))
# print(ac_1.withdraw(50000))
# try:
#     print(ac_1.withdraw(2000))
# except NotEnoughBalance as e:
#     print(e)
# try:
#     print(ac_1.withdraw(1000))
# except NotEnoughBalance as e:
#     print(e)








ac_1 = Account()
ac_1.deposit(50000)
ac_1.withdraw(50000)
ac_1.withdraw(2000)
ac_1.withdraw(1000)
