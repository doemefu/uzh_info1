#!/usr/bin/env python3
from unittest import TestCase

from script import flatten_list


# This test suite only tests one simple example and whether
# the value returned by the solution function has the correct
# type. If this test passes, it does not mean that you will
# get any points. The grading system uses different, more
# exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".


class PublicTestSuite(TestCase):
    def test_correct_return_type(self):
        nested_list = [1, [8, 4], 2, 3]
        actual = flatten_list(nested_list)
        self.assertIsInstance(actual, list)
