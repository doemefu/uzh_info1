#!/usr/bin/env python3

# Count the number of recursive calls.
# Not relevant to solve the exercise but just to show the performance improvement.
count = 0


# Change the functions below to calculate the knapsack value.
# Use the variable lookup_table to store intermediate results to improve performance.
# Don't forget to pass it as an argument to the recursive calls.
def knapsack(capacity, weights, values, lookup_table=None):
    # Only for performance measurement. You can ignore this line or event remove it.
    global count
    count += 1

    # Initialize lookup table on the first call
    if lookup_table is None:
        lookup_table = {}

    # You need to change the following part of the function

    return -1


if __name__ == "__main__":
    # The following lines call the function and prints the return
    # value to the Console. This way you can check what it does.
    print("The maximum value in the knapsack is:", knapsack(50, (10, 20, 30), (60, 100, 120)))
    print("Number of function calls:", count)
