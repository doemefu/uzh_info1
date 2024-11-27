# Blackbox Testing 'Sorted Arrays Overlap'

This task ia about *black-box testing* of a function based on its specification
and without any knowledge about its implementation.

### Function Specification

The function under test `sorted_arrays_overlap` takes two arrays as parameters and 
retrieves elements that are present in both arrays.

A correct implementation of `sorted_arrays_overlap` must comply with the following requirements:

Input:

The function takes two parameters called `array_1` and `array_2`:
* These arrays are non-empty lists of any integers sorted in ascending order.
* Arrays may have different length and may have duplicate elements.

Output:

The function returns:
- a string `Invalid input types! Both parameters should be arrays.` if either of the arguments is not of type `list`.
- a string `Empty arrays! Neither of the arrays can be empty.` if either of the arguments is an empty list.
- a string `Invalid data types within arrays! Arrays should contain only integers.` if either of the passed lists contains non-integer elements.
- a string `Not sorted arrays! Both arrays should be sorted in ascending order.` if either of the passed lists is not sorted in ascending order.
- a string `There are no overlapping elements in given arrays.` if there are no same elements in the arrays.
- a list containing elements that represent an intersection of the two arrays if the arguments passed to a function are valid.

Examples:

```Python
array_1 = [-5, -3, -1, 7, 8, 14, 19]
array_2 = [-8, -5, -2, -1, 19]
result = sorted_arrays_overlap(array_1, array_2)
print(result)  # [-5, -1, 19]
```

```Python
array_1 = [5, 8, 14, 19, 19, 19, 23, 34, 52]
array_2 = [2, 5, 7, 8, 15, 19, 19, 25, 34, 62]
result = sorted_arrays_overlap(array_1, array_2)
print(result)  # [5, 8, 19, 19, 34]
```

### Task

Your task is to provide a comprehensive test suite in `task/tests.py` that checks whether an implementation 
of `sorted_arrays_overlap` follows the specification given above. Try to find as many corner cases as possible
and write a corresponding test for each of them. 

Your test suite will be run with a variety of correct and incorrect implementations.
The resulting grade depends on its ability to detect faulty implementations of the function.
More specifically, the test suite should pass for a correct implementation and fail for an incorrect one.

**Note:** You do not need to implement `sorted_arrays_overlap` in `task/script.py`. 
You can simply start writing your tests against an unknown implementation. However, it might be useful 
to write a correct implementation of the function, so you can make sure your test cases work as expected. 
Nevertheless, your implementation of the function is irrelevant for the grading.

**Note:** You do not need to come up with good error messages, it is enough to fail a test if a problem 
can be detected (e.g., `self.assertEquals(expected, actual)`).

**Note:** Define your test suite as a subclass of `TestCase`.
Do not use utility functions for the assertions, instead, include calls like `self.assertEqual` 
directly in the body of the test functions, or the automated grading will mark the solution as incorrect.

**Note:** The provided files define the signatures of various classes and functions.
Do not change these signatures, or the automated grading will fail.
