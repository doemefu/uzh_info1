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

    # Base case: no items or no capacity
    if capacity == 0 or not weights:
        return 0

    # Check if result is already computed
    if (capacity, len(weights)) in lookup_table:
        return lookup_table[(capacity, len(weights))]

    # Item fits in knapsack
    if weights[0] <= capacity:
        # Calculate the value of the knapsack if we take the item
        take_item = values[0] + knapsack(capacity - weights[0], weights[1:], values[1:], lookup_table)
        # Calculate the value of the knapsack if we do not take the item
        dont_take_item = knapsack(capacity, weights[1:], values[1:], lookup_table)

        # Store and return the maximum of taking and not taking the item in the lookup table
        lookup_table[(capacity, len(weights))] = max(take_item, dont_take_item)
        return lookup_table[(capacity, len(weights))]

    # Item does not fit in knapsack anymore, just skip it and continue with the next item
    lookup_table[(capacity, len(weights))] = knapsack(capacity, weights[1:], values[1:], lookup_table)
    return lookup_table[(capacity, len(weights))]


if __name__ == "__main__":
    # The following lines call the function and prints the return
    # value to the Console. This way you can check what it does.
    print("The maximum value in the knapsack is:", knapsack(50, (10, 20, 30), (60, 100, 120)))
    print("Number of function calls:", count)
