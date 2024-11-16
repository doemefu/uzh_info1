#!/usr/bin/env python3
from unittest import TestCase

import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

class PublicTestSuite(TestCase):

    def test_case0(self):
        actual = script.sieve_of_eratosthenes(13)
        self.assertEqual(actual, [2, 3, 5, 7, 11, 13])

