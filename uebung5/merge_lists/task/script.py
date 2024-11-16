#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    if not a or not b:
        return []

    mi = min(len(a), len(b))
    myList = [(a[i], b[i]) for i in range(mi)]  # Merge common indices

    # Add remaining elements from the longer list
    if len(a) > len(b):
        myList += [(a[i], b[mi-1]) for i in range(mi, len(a))]
    elif len(b) > len(a):
        myList += [(a[mi-1], b[i]) for i in range(mi, len(b))]

    return myList



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
