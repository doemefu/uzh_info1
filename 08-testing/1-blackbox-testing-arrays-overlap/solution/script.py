#!/usr/bin/env python3


def sorted_arrays_overlap(array_1, array_2):
    if not isinstance(array_1, list) or not isinstance(array_2, list):
        return "Invalid input types! Both parameters should be arrays."

    if not array_1 or not array_2:
        return "Empty arrays! Neither of the arrays can be empty."
    elif not all(type(x) == int for x in array_1) or not all(type(x) == int for x in array_2):
        return "Invalid data types within arrays! Arrays should contain only integers."
    elif not (array_1 == sorted(array_1)) or not (array_2 == sorted(array_2)):
        return "Not sorted arrays! Both arrays should be sorted in ascending order."
    else:
        i, j = 0, 0
        overlap = []

        while i < len(array_1) and j < len(array_2):
            if array_1[i] == array_2[j]:
                overlap.append(array_1[i])
                i += 1
                j += 1
            elif array_1[i] < array_2[j]:
                i += 1
            else:
                j += 1

        return overlap if overlap else "There are no overlapping elements in given arrays."


#     # Example usage:
#
#
# A = [1, 2, 4, 5, 6]
# B = [2, 3, 5, 7]
# result = intersection_sorted_arrays(A, B)
# print(f"Intersection: {result}")
