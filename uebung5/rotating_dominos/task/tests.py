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
    def test_return_type(self):
        top = [2, 2, 2, 1, 2, 2]
        bottom = [5, 6, 4, 2, 3, 2]
        self.assertIsInstance(script.min_domino_rotations(top, bottom), int)

    def test_return_1(self):
        top = [2, 2, 2, 1, 2, 2]
        bottom = [5, 6, 4, 2, 3, 2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 1)

    def test_return_2(self):
        top = [2, 2, 2, 2, 2, 2]
        bottom = [5, 6, 4, 2, 3, 2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_return_3(self):
        top = [5, 6, 4, 2, 3, 2]
        bottom = [2, 2, 2, 2, 2, 2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

        # New test cases for various edge cases

    def test_empty_lists(self):
        top = []
        bottom = []
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_single_element_identical(self):
        top = [2]
        bottom = [2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_single_element_different(self):
        top = [2]
        bottom = [3]
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_impossible_case(self):
        top = [1, 2, 3, 4, 5, 6]
        bottom = [6, 5, 4, 3, 2, 1]
        self.assertEqual(script.min_domino_rotations(top, bottom), -1)

    def test_mixed_domino(self):
        top = [1, 2, 3, 2, 2, 2]
        bottom = [2, 2, 2, 4, 3, 2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 2)

    def test_already_all_equal(self):
        top = [2, 2, 2, 2, 2, 2]
        bottom = [2, 2, 2, 2, 2, 2]
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_case_with_large_input(self):
        top = [1] * 1000
        bottom = [1] * 1000
        self.assertEqual(script.min_domino_rotations(top, bottom), 0)

    def test_case_with_rotations_needed(self):
        top = [1, 1, 1, 1, 2, 1, 1]
        bottom = [2, 1, 1, 1, 1, 1, 1]
        self.assertEqual(script.min_domino_rotations(top, bottom), 1)