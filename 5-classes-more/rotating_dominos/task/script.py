#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):

    counter_top = {1:0,2:0,3:0,4:0,5:0,6:0}
    counter_bottom = {1:0,2:0,3:0,4:0,5:0,6:0}

    for a in top:
        counter_top[a] += 1

    for b in bottom:
        counter_bottom[b] += 1

    #print(counter_top)
    #print(counter_bottom)

    key_top = max(counter_top, key=counter_top.get)
    key_bottom = max(counter_bottom, key=counter_bottom.get)

    #print(key_top)
    #print(key_bottom)

    op1 = len(top) - counter_top[key_top]
    op2 = len(bottom) - counter_bottom[key_bottom]

    if len(top) != len(bottom):
        return -1
    elif len(top) == 1:
        return 0
    elif counter_top[key_top] + counter_bottom[key_top] >= len(top) or counter_bottom[key_bottom] + counter_top[key_bottom] >= len(bottom):
        #print("gud")
        return op1 if op1<op2 else op2
    else:
        #print("not gud")
        return -1




# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

#print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
#print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
#print(min_domino_rotations([1, 1, 1, 1, 2, 1, 1], [2, 1, 1, 1, 1, 1, 1]))
