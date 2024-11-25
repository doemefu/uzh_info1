# Bank Account Class

In this task, you will learn how classes work in Python, including the use of `__init__`, `__str__`, and `__repr__`
methods.

You will implement a simple bank account class that can perform basic operations such as depositing and withdrawing
money.

## Task

Create a class named `BankAccount` with the following specifications:

- **Attributes:**

    - `_owner`: A string representing the name of the account owner.

    - `_balance`: A float representing the current balance of the account.

- **Methods:**

    - `__init__(self, owner, balance=0.0)`: Initializes a new `BankAccount` instance with the given owner and optional
      initial balance (default is `0.0`).

    - `deposit(self, amount)`: Adds the given `amount` to the account balance.

        - If the `amount` is less than or equal to zero, raise a `ValueError` with the messsage
          `"Deposit amount must be positive"`.

    - `withdraw(self, amount)`: Subtracts the given `amount` from the account balance.

        - If the `amount` is less than or equal to zero, raise a `ValueError` with the message
          `"Withdrawal amount must be positive"`.

        - If the `amount` exceeds the current balance, raise a `ValueError` with the message `"Insufficient funds"`.

    - `__str__(self)`: Returns a user-friendly string representation of the account in the format:

      ```
      Account owner: {owner}
      Account balance: CHF {balance}
      ```

    - `__repr__(self)`: Returns an unambiguous string representation of the account, in the format:

      ```
      BankAccount('{owner}', {balance})
      ```

## Optional

- To learn more about the built-in functions, refer to the documentation:
    - [\_\_init__()](https://docs.python.org/3/reference/datamodel.html#object.__init__)
    - [\_\_str__()](https://docs.python.org/3/reference/datamodel.html#object.__repr__)
    - [\_\_repr__()](https://docs.python.org/3/reference/datamodel.html#object.__repr__)

- In the `test.py` file, there are two simple unit tests for illustration purposes. You can add more tests to ensure
  that your implementation is correct.
