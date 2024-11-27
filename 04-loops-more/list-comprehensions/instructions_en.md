In this task, you will practice list comprehensions.

In `script.py`, you can find six functions. The first function, `square_numbers` has already been implemented as an example. It takes a parameter `numbers` which is a list of integers and returns a list where each number is squared.

The other functions are for you to implement. Remember that you can always add `print` statements at the bottom to call your implementation, for example:

```
print(square_numbers([1, 2, 3]))
```

**Important:** all functions *must* start with a `return` statement and they *must* return a list comprehension, just as demonstrated in `square_numbers`. Replace `pass` with your return statement; do not declare any variables; construct and return a list comprehension outright.

Implement the following 5 functions:

* `even_numbers(numbers)` should return a list of all numbers from `numbers` which are even. The resulting list should be a subset of the original list.

* `all_even(numbers)` should return a list where all numbers are converted using the following strategy: `round` the value. If the rounded value is odd, add `1` to the value and round it again (this will result in an even number). The lengths of the original list and the resulting list should be equal.

* `only_integers(numbers)` should return a list of all numbers that are integers from the original list. The resulting list should be a subset of the original list. `example: only_integers([1.1, 2]) => [2]`

* `only_positive(numbers)` should return a list where all the numbers from `numbers` have been converted to positive. The resulting list and the original list should have the same length.

* `from_1_to_1000_containing_a` should return a list of all numbers up to a thousand that somewhere contain the number `a`. `example: from_1_to_1000_containing_a(2) => [2, 12, 20, ...]`. Note that this function does not take `numbers`, and that `a` may have multiple digits (e.g. `25`).

* ` multiple_of_a_and_greater_than_b(numbers, a, b)` takes two additional inputs `a` and `b`. They are both positive integers. The resulting list should contain all the numbers from `numbers` that are a multiple of `a` and greater than `b`.
