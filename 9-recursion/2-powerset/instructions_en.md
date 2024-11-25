# Generating the Power Set of a Given Set

This task focuses on implementing a recursive function to generate the [power set][power-set] of a given set of unique elements.
The power set includes all subsets ranging from the empty set to the set itself.

Write a program that defines a function powerset(nums) which takes a list of integers as input and returns all possible subsets of these integers.
- If the input list is empty, the function should return a list containing an empty list.
- Ensure that the function removes duplicates if the input list contains any.

**Note:** Make sure that your solution is self-contained within the `powerset` function.
You may test your solution with different inputs, but do not change the name of the main function or the automated grading will fail.

**Note:** Use recursion to build the power set by considering whether to include or exclude each element.

[power-set]: https://en.wikipedia.org/wiki/Power_set