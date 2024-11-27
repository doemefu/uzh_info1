#!/usr/bin/env python3
from unittest import TestCase

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

import script

class PublicTestSuite(TestCase):
    def test_return_type(self):
        actual = script.total_sum_repaid("lump_sum")
        self.assertTrue(callable(actual))
