#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    returnDict = {}

    for a in d.items():
        if a[1] in returnDict:
            returnDict[a[1]].append(a[0])
        else:
            returnDict[a[1]] = [a[0]]

    for key in returnDict:
        returnDict[key] = sorted(returnDict[key])

    return returnDict





# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
