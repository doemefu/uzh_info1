#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    numbers = set()
    for c in range(0,10):
        for p in range(2,11):
            s = n[0:p] + str(c) + n[p:10]
            numbers.add(s)

    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet
    possible_nrs_for_juliet = []

    for a in numbers:
        if a in wa_nrs:
            possible_nrs_for_juliet.append(a)

    return [a for a in numbers if a in possible_nrs_for_juliet]

    #return possible_nrs_for_juliet
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
