Hiding complexity behind simple class interfaces facilitates the life of developers tremendously.

For example, imagine the hassle if you had to build a correct matrix representation and always calculate multiplications
and additions manually by multiplying or adding up individual values. Instead, what you would do normally,
is to just use a calculator that allows to fill in the matrix values without ever worrying about the internal
calculation steps performed or the checks done to ensure correctness.

Thus, in this task you will build a class `Matrix` with basic capabilities of multiplication and addition to illustrate
these steps usually just abstracted away by a calculator.

## Specification
 * The constructor for `Matrix` should take nested lists defining the matrix, i.e.:

```
 m = Matrix(
    [[1,2],
     [3,4]])
```

 * Each nested list corresponds to one row in the matrix
 * The indices within a nested list correspond to the columns.
 * If the constructor input satisfies the following properties it should be stored as a **private** instance variable:
    1. It contains exactly 2 dimensions.
    2. All values contained in nested lists are integers and/or floats.
    2. All nested lists have the same length.
    3. There has to be at least one non-empty row (in other words: `[[]]` would be invalid).
 * If the above conditions are not satisfied, an `AssertionError` should be thrown
(you may use the `assert x == y, "error message in case of assertion failure"` syntax).
 * Implement `__add__` so that two instances of class `Matrix` can be added via the `+` operator.
 * Implement `__mul__` so that two instances of class `Matrix` can be multiplied via the `*` operator.
 * Implement `__eq__` so that two instances of class `Matrix` can be compared via the `==` operator.
 * Implement `__hash__` so that instances of class `Matrix` can be used as dictionary keys.


**Note:** In case you do not know how to add/multiply matrices, check this [Link](https://en.wikipedia.org/wiki/Matrix_(mathematics)#Matrix_multiplication)

**Note:** To read more about `__add__` and `__mul__`, checkout the [appropriate documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

**Note:** We encourage you to experiment with your data structure to understand the effect that providing the various methods has on the way in which you can use your data structure.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.
