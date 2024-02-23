class SavingsAccount:
    """This is the Parent class of this program."""
    def __init__(self, account_no):
        """Initialize attributes.
            The initial balance is 1000 taka when an account is opened."""
        self.account_no = account_no
        self.balance = 1000
        self.withdrawals = 0

    def withdraw(self, amount):
        """
        1. Checks if more than 3 times of withdrawals have been done this month.
        2. If [1] is true then an additional 10 taka fee will be charged.
        3. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        4. If [3] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if (self.withdrawals >= 3):
            if ((self.balance - amount) >= 1010):
                self.withdrawals += 1
                self.balance -= (amount + 10 )
                print(f"An additional 10 taka has been charged as this is \nyour {self.withdrawals}th withdraw this month!")
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!")
        else:
            if ((self.balance - amount) >= 1000):
                self.withdrawals += 1
                self.balance -= amount
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!!!")
    
    def deposite(self, amount):
        """Deposits the required amount to the account and incriment the balance."""
        self.balance += amount
        print(f"[{amount} taka] has been deposited to [Account no:{self.account_no}]")

    def profit(self):
        """ 5% per year profit!
            [Profit = Deposit x Interest Rate x Time]
            Interest Rate = 5%
            Time = 1 year """
        profit = self.balance * 0.05 * 1
        self.balance += profit
        return f"Your profit for this year is {profit}"

    def reset_withdrawals(self):
        """Resets withdrwals attributes every month."""
        self.withdrawals = 0

    def __str__(self):
        return f"Account No: {self.account_no} \nBalance: {self.balance}"


class CurrentAccount(SavingsAccount):
    """This is the Child class of (SavingsAccount) class."""
    def __init__(self, account_no):
        """Calls the super().__init__ function to get access to all the methods and attributes of the parent class"""
        super().__init__(account_no)

    def withdraw(self, amount):
        """
        ## This method overrid the method form the parent class ##
        1. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        2. If [1] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if ((self.balance - amount) >= 1000):
            self.balance -= amount
        else:
            print(f"Transaction failed!!! You don't have sufficient balance!!!")

    def profit(self):
        """ 
        ## This method overrid the method form the parent class ##
        3% per year profit!
        [Profit = Deposit x Interest Rate x Time]
        Interest Rate = 5%
        Time = 1 year
        """
        profit = self.balance * 0.03 * 1
        self.balance += profit
        return f"Your profit for this year is {profit}"
    
"""
Here - the SavingsAccount class is the parent class and
the CurrentAccount class is the child class.
The withdraw and profit methods will overrid the parent class
methods and will be used from the child class if called by the
intences of the child class.
"""


account_1 = SavingsAccount("0152330101")
print(account_1)
account_1.deposite(50000)
print(account_1)
account_1.withdraw(10000)
print(account_1)
account_1.withdraw(10000)
print(account_1)
account_1.withdraw(10000)
print(account_1)
account_1.withdraw(10000)
print(account_1)
account_1.withdraw(5000)
print(account_1)
account_1.withdraw(5000)
print(account_1)
print(account_1.profit())
print(account_1)
account_1.withdraw(5000)
print(account_1)
account_1.deposite(10000)
print(account_1)
account_1.reset_withdrawals()
account_1.withdraw(5000)
print(account_1)


print("\n2nd Account:=>\n")
account_2 = CurrentAccount("0152330116")
print(account_2)
account_2.deposite(100000)
print(account_2)
account_2.withdraw(10000)
account_2.withdraw(10000)
account_2.withdraw(10000)
account_2.withdraw(10000)
account_2.withdraw(10000)
print(account_2)
print(account_2.profit())
print(account_2)