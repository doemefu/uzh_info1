#!/usr/bin/env python3

# recursive solution
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# iterative solution
def factorial(n):
    result = 1
    for number in range(1, n+1):
        result *= number
    return result

# correct solution if this weren't a programming exercise :o)
#from math import factorial

