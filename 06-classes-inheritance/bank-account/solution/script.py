#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods or variables though.
class BankAccount:
    def __init__(self, owner, balance=0.0):
        # You need to change the following part of the function
        # to instantiate class variables.
        # Trailing underscore is a convention to indicate a private variable.
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        # You need to change the following part of the function
        # to implement the deposit logic.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        # You need to change the following part of the function
        # to implement the withdrawal logic.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self):
        # You need to change the following part of the function
        # to implement the correct string representation.
        return f"Account owner: {self._owner}\nAccount balance: CHF {self._balance}"

    def __repr__(self):
        # You need to change the following part of the function
        # to implement the correct representation of the object.
        return f"BankAccount('{self._owner}', {self._balance})"


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
if __name__ == "__main__":
    my_account = BankAccount("Melon Tusk", 269800000000)
    my_account.withdraw(200000000000)
    print(my_account)
    print(repr(my_account))
