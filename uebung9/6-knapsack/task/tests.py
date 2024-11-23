#!/usr/bin/env python3
from unittest import TestCase

from script import knapsack


# This test suite only tests one simple example and whether
# the value returned by the solution function has the correct
# type. If this test passes, it does not mean that you will
# get any points. The grading system uses different, more
# exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

#!/usr/bin/env python3
from unittest import TestCase

from script import knapsack


class PublicTestSuite(TestCase):
    # Helper function to check return type
    def _check_return_type(self, actual, expected):
        m = f"Your function should return a {type(expected)} but returned a {type(actual)}!"
        self.assertIsInstance(actual, type(expected), m)

    # Public test cases
    def test_knapsack(self):
        expected = 220
        actual = knapsack(50, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} but returned {actual}!"
        self._check_return_type(actual, expected)
        self.assertEqual(expected, actual, msg=m)

    def test_empty_items(self):
        expected = 0
        actual = knapsack(50, [], [])
        m = f"Your function should return {expected} for an empty list of items but returned {actual}!"
        self._check_return_type(actual, expected)
        self.assertEqual(expected, actual, msg=m)

    def test_zero_capacity(self):
        expected = 0
        actual = knapsack(0, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} when capacity is 0 but returned {actual}!"
        self._check_return_type(actual, expected)
        self.assertEqual(expected, actual, msg=m)

    def test_single_item_fits(self):
        expected = 60
        actual = knapsack(10, [10], [60])
        m = f"Your function should return {expected} for a single item that fits but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_single_item_does_not_fit(self):
        expected = 0
        actual = knapsack(5, [10], [60])
        m = f"Your function should return {expected} for a single item that does not fit but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_multiple_items_exact_fit(self):
        expected = 160
        actual = knapsack(30, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} for items that exactly fit the capacity but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_multiple_items_partial_fit(self):
        expected = 220
        actual = knapsack(50, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} for items that partially fit the capacity but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_multiple_items_with_excess_capacity(self):
        expected = 280
        actual = knapsack(100, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} for items with excess capacity but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_duplicate_items(self):
        expected = 220
        actual = knapsack(50, [10, 10, 20], [60, 60, 100])
        m = f"Your function should return {expected} for duplicate items but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_large_capacity(self):
        expected = 280
        actual = knapsack(60, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} for a large capacity but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_large_weights(self):
        expected = 0
        actual = knapsack(5, [10, 20, 30], [60, 100, 120])
        m = f"Your function should return {expected} when all items exceed the capacity but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)

    def test_high_value_low_weight_items(self):
        weights = [1, 2, 3, 50, 100]
        values = [1000, 900, 800, 1, 1]
        capacity = 6
        expected = 2700  # First three items (1+2+3 = 6 weight, 1000+900+800 = 2700 value)
        actual = knapsack(capacity, weights, values)
        m = f"Your function should return {expected} for high-value, low-weight items but returned {actual}!"
        self._check_return_type(expected, actual)
        self.assertEqual(expected, actual, msg=m)
