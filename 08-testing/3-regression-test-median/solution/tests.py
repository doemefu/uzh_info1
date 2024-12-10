#!/usr/bin/env python3
from unittest import TestCase
from task.script import median


class PrivateTestSuite(TestCase):

    def test_median_works_for_single_elements(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists(self):
        self.assertEqual(3, median([5, 1]))

    # The following were added based on the bug reports. Many
    # alternatives exist to test for the same properties.

    def test_median_works_for_uneven_lists(self):
        self.assertEqual(2.5, median([1, 4]))

    def test_median_works_for_floats(self):
        self.assertEqual(3.4, median([3.4, 1.2, 5.6]))

    def test_median_works_for_empty_lists(self):
        # the behavior for empty lists should be defined as well
        # which default you choose depends on you, the important
        # property is that the call to median([]) does not crash
        self.assertEqual(None, median([]))