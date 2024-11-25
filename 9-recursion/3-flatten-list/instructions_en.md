# Flatten List

Your task is to implement a recursive function `flatten_list`:

Argument:
- the function takes a list as an argument, this list can be arbitrarily deeply nested
- input list can contain elements of different types
- it's guaranteed that the list won't contain elements of a collection type (tuple, set, dictionary) 
other than a list; you don't have to check it
- the only check you need to add is whether the passed argument is of type list:
  - in case it's not a list, raise a `TypeError` with the following error message: `"Expected argument has to be a list."`

Return:
- the function returns a flatted version of the passed list: returned list should not contain any nested lists.


**Note:** Make sure that your solution is self-contained within the `flatten_list` function.
You may test your solution with different inputs, but do not change the name of the main function or the automated grading will fail.

**Note:** Use recursion. Solutions without recursion will not receive any points.
