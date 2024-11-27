
In this task you are going to practice *black-box testing*, i.e., you will test a function, just based on its specification and with knowledge from the domain, but without knowing a concrete implementation.

Assume that you are repsonsible for testing a `sort` function, which is being provided by a third party. The implementation should be consistent with the following specification:


    == Specification of `sort` ==
     
    - takes an `Iterable` as a parameter that contains comparable elements
    - sorts all contained elements without changing the original `Iterable`
    - elements should be sorted in ascending order (i.e., smallest first)
    - always returns a new `List` that contains the sorted elements
    - If parameter is `None` or non-iterable, return  `None`.

    The implementaion can assume that all elements of a provided iterable
    are comparable data types (e.g., int, float, string). This means that
    relational operations like '<', '>', etc. are defined. The behavior
    for data types that are not comparable is not defined and they do not
    need to be handled.

Your task is to provide a good test suite (`public/tests.py`) that can decide whether a given `sort` implementation follows this specification. For the grading, your test suite will be run with a variety of correct and incorrect implementations. The resulting grade depends on the ability of the test suite to classify these cases correctly. More specifically, the test suite should pass for a correct implementation and fail for an incorrect one.

**Note:** You do not need to come up with good error messages, it is enough to fail a test if a problem can be detected (e.g., `self.assertEquals(expected, actual)`).

**Note:** Define your test suite as a subclass of `TestCase`. Do not use utility functions for the assertions, instead, include calls like `self.assertEqual` directly in the body of the test functions or the automated grading will mark the solution as incorrect.

**Note:** You can implement `sort` in the `public/script.py` file, "Test&Run" will then execute your test suite. However, you are encouraged to provide the test suite first. The goal is to practice the identification of interesting test cases, indepedently of a concrete implementation. Your `script.py` is irrelevant for the grading.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.
