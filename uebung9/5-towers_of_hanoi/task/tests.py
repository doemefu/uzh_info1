#!/usr/bin/env python3

from unittest import TestCase
from task.script import req_steps


class PublicTestSuite(TestCase):

    # If this test passes, that does not mean that you will get any points.
    # The grading system uses different, more exhaustive tests.

    # Feel free to extend the class with your own test cases,
    # which will then also be executed in every "Test & Run".

    def test1(self):
        n = 3
        expected = 7
        actual = req_steps(n)
        m = "The calculation is not correct for {} disks.".format(n)
        self.assertEqual(expected, actual, m)

