#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def factorial(n):
    # implement this function
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
num = 8
print(f"factorial({num}) = {factorial(num)}")

