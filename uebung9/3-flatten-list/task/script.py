#!/usr/bin/env python3

# Change the functions below to flatten a given nested  list.
def flatten_list(nested_list):
    pass


# The following lines call the function and print the return
# value to the Console. This way you can check what they do.
nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
flat_list = flatten_list(nested_list)
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8]


nested_list_2 = [[4.5, 6, "string"], "d", "g", ["f", 1, 6, ["another_string"]]]
flat_list_2 = flatten_list(nested_list_2)
print(flat_list_2)  # [4.5, 6, "string", "d", "g", "f", 1, 6, "another_string"]
