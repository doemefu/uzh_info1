#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    # implement this function
    if n == 1:
        return("1 is the multiplicative identity")


    for val2 in range((n-1),1,-1):
        print(val2)
        if n % val2 == 0:
            val1 = n / val2
            return(f"{n} is not a prime number ({val1:.0f} * {val2:.0f} = {n})")

    return(f"{n} is prime")


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(is_prime(12))

