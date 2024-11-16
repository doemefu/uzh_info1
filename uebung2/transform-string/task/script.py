#!/usr/bin/env python3


# perform the transformation
def transform_string(s):
    # Insert your code here.
    # Maybe you will want to use a temporary variable to hold the index
    # of the ":" character, so you can use it afterwards to slice the string?
    slice = s.find(":")
    start = s[0:slice]
    end = s[slice+1:len(s)]
    start2 = start.lower()
    end2 = end.upper()

    return start2 + ":" + end2

# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string("aB:cD"))

