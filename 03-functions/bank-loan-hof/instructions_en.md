# Bank Loan

In programming languages, there exist two types of functions:
- **first-order functions**: these functions **cannot** take other functions as arguments or return them as a result;
- **higher-order functions**: these functions **can** take one or more functions as arguments and/or
return them as a result. Functions that can be passed as arguments or returned as a result are called **first-class functions**.

Python supports **higher-order functions** and, thus, **first-class functions**, and the goal of the current task is to demonstrate 
one particular aspect of this concept, namely, that a function can be a return value of another function.
This will be done through writing a small program related to bank loans. 

When taking a loan from a bank, the borrower has eventually to repay that loan (called principal) to the bank, 
plus it has to pay interest amount on top of the principal. The interest amount depends on the principal, 
interest rate, number of periods, and a payment schedule that can be:

1. **Lump sum** payment: the principle is paid once at the end of the whole borrowing period (for example, at the end of the year). 
In this case, the interest amount is equal to the product of the principal, monthly interest rate and the number of periods (months) 
contained in the whole borrowing period (year). To get the total sum returned to the bank, we need to sum up 
the interest amount and the principal.


2. **Annuity** payments: the debt is paid equally every month; 
every (annuity) payment contains a part of the principal and the corresponding interest amount. The formula for the annuity payment is:

![Formula](resource/formula.png)

where:
- A = monthly annuity payment amount
- P = loan principal
- r = monthly interest rate
- n = total number of payments (months)

To calculate the total sum paid back to the bank, the annuity payment has to 
be multiplied by the total number of payments (months).

Given `principal`, `interest_rate`, and `number_periods`, implement the following functions that calculate the total 
amount repaid to the bank based on the payment schedule described above:

- `lump_sum(principal, interest_rate, number_periods)`
- `annuity(principal, interest_rate, number_periods)`

Then, implement a function `total_sum_repaid(payment_type)` which takes `payment_type` of type `str` 
as an argument (can be equal to either "annuity" or "lump_sum"). The function should **return one of the functions** implemented above 
depending on the passed parameter.
In case of invalid `payment_type`, return a string "Invalid payment type. Allowed payment types are: annuity or lump_sum!".

Please, make sure that your solution is self-contained within the `total_sum_repaid` function and the two additional functions 
`lump_sum` and `annuity`. You may test your solution with different inputs, but please, do not change functions' signatures.
