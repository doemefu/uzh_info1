#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    if len(data) == 0:
        return(((), []))
    keytuple = sorted(data[0])
    valueList = []
    for item in data:
        valueList.append(tuple([item[key] for key in keytuple ]))
    return((tuple(keytuple),valueList))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    
]
print(compress(data))



