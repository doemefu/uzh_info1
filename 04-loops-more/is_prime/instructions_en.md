A prime number is a number greater than 1 that can only be divided by itself and by 1. Write a function `is_prime` that takes a _positive_ integer as an argument and checks whether it is prime or not.

Depending on the result, the function should return the strings `x is prime` (for prime numbers) or `x is not a prime number (a * b = x)`, with the smallest possible `a` (for non-prime numbers), showing the actual values for `x`, `a` and `b`. For example, calling `is_prime(12)` should return the string `12 is not a prime number (2 * 6 = 12)`. By definition, `1` is not a prime number, the function should return the string `1 is the multiplicative identity`. You can assume that only values greater than 0 will be passed to this function.

**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

