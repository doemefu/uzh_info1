#!/usr/bin/env python3
from math import ceil, sqrt

# As mentioned in the hints, you might want to use the math package
import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.
    max_search = ceil(sqrt(n))
    prime_list=[*range(2,n+1)]

    for b in range(1, n):
        if b in prime_list:
            for a in range(2*b, n+1, b):
                prime_list.remove(a) if a in prime_list else True
        elif b > max_search:
            return prime_list

    return prime_list

    # You don't need to change the following line.
    # It simply returns the list created above.
    #return primes_up_to_n

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(1000))
