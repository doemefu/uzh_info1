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
    def _check_return_type(self, actual, expected):
        m = f"The standard_tax() function should return a {type(expected)} but returned a {type(actual)}!"
        self.assertIsInstance(actual, type(expected), m)

    # This is an actual test. Tests in unittest must start with "test_".
    # This test will be executed automatically by unittest.
    def test_correct_tax_value(self):
        expected = 8.2
        actual = script.calculate_tax(101, script.standard_tax)
        m = f"The calculate_tax() function should return {expected} but returned {actual}!"
        self._check_return_type(actual, expected)
        self.assertEqual(actual, expected, msg=m)
