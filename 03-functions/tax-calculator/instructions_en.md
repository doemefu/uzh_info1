# Tax Calculator

In this task, you will learn how function passing works.
You will implement a tax calculator that calculates the corresponding tax based on different tax rates.

In Switzerland, there are three different tax rates:

- **Standard Tax Rate**: **8.1%**
- **Reduced Tax Rate**: **2.5%**
- **Accommodation Tax Rate**: **3.7%**

Given an `amount`, your task is to implement the following functions, which return the calculated tax amount based on
the tax rate:

- `standard_tax(amount)`
- `reduced_tax(amount)`
- `accommodation_tax(amount)`

Finally, you will implement the function `calculate_tax(amount, tax_type)` which takes an `amount` and a `tax_type`
function as parameters. If the `amount` is less than or equal to zero, the function should return `0.0`. Otherwise, 
the function should calculate the tax by calling the `tax_type` function with `amount` as the argument and return the
calculated tax amount **rounded to the nearest 0.05 increment**.

## Rounding Behaviour

- 10 --> 10.0
- 10.12 --> 10.1
- 10.23 --> 10.25
- 10.37 --> 10.35
- 10.48 --> 10.5

## Optional

- To learn more about Floating-Point Arithmetic in Python, you can read the following article: [Floating-Point 
Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html).

- In the `test.py` file, there are two simple unit tests for illustration purposes. You can add more tests to ensure 
  that your implementation is correct.
