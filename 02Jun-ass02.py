class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw of {self.amount}"

class InvalidDepositError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid Deposit {self.amount} . Minimum is 1"
class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.__balance = balance  # Private attribute

    # Methods
    def deposit(self, amount):
        if amount < 1 :
            raise InvalidDepositError(amount)
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise InsufficientFundsError(amount, self.__balance)

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Steve")  # Create an object
try:
    a1.deposit(0)  # Call method
    print("Valid Deposit:")
    try:
        a1.withdraw(50000)
        print("Shopping!")
    except InsufficientFundsError as ex:\
        print(ex)
    print(a1.getbalance())
except InvalidDepositError as ex:
    print(ex)
