#!/usr/bin/env python3
from unittest import TestCase

from task import script


# This test suite only tests one simple example and whether
# the value returned by the solution function has the correct
# type. If this test passes, it does not mean that you will
# get any points. The grading system uses different, more
# exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".


class PublicTestSuite(TestCase):
    # This is just a helper function and not an actual test.
    # Therefore, it will not be executed automatically by unittests
    # but rather be called from another test method.
    def _assert_return_type(self, actual, expected):
        m = f"The powerset(nums) function should return a {type(expected)} but returned a {type(actual)}!"
        self.assertIsInstance(actual, type(expected), m)

    # This is an actual test. Tests in unittest must start with "test_".
    # This test will be executed automatically by unittest.
    def test_powerset(self):
        test_set = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        actual = script.powerset(test_set)
        self._assert_return_type(actual, expected)
        m = f"The powerset(nums) function should return '{expected}' but returned '{actual}'"
        self.assertEqual(actual, expected, m)
