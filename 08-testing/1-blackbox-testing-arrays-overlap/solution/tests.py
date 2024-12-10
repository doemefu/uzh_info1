#!/usr/bin/env python3

from unittest import TestCase
from task.script import sorted_arrays_overlap


class SampleSortedArraysOverlapTest(TestCase):

    def sorted_arrays_overlap_test_class(self, array_1, array_2):
        if not isinstance(array_1, list) or not isinstance(array_2, list):
            return "Invalid input types! Both parameters should be arrays."

        if not array_1 or not array_2:
            return "Empty arrays! Neither of the arrays can be empty."
        elif not all(type(x) == int for x in array_1) or not all(type(x) == int for x in array_2):
            return "Invalid data types within arrays! Arrays should contain only integers."
        elif not (array_1 == sorted(array_1)) or not (array_2 == sorted(array_2)):
            return "Not sorted arrays! Both arrays should be sorted in ascending order."
        else:
            i, j = 0, 0
            overlap = []
            while i < len(array_1) and j < len(array_2):
                if array_1[i] == array_2[j]:
                    overlap.append(array_1[i])
                    i += 1
                    j += 1
                elif array_1[i] < array_2[j]:
                    i += 1
                else:
                    j += 1
            return overlap if overlap else "There are no overlapping elements in given arrays."

    # 2g
    def test_01_return_type_valid(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23, 34, 52]
        array_2 = [1, 2, 5, 7, 8, 15, 19, 25, 34, 62]
        actual = sorted_arrays_overlap(array_1, array_2)
        self.assertIsInstance(actual, list)
        self.assertTrue(actual)

    #  Invalid input (1a): not arrays
    def test_02_invalid_input_not_arrays(self):
        array_1 = "[1, 3, 5, 7, 8, 14, 19, 23, 34, 52]"
        array_2 = [1, 2, 5, 7, 8, 15, 19, 25, 34, 62]
        actual_1 = sorted_arrays_overlap(array_1, array_2)
        actual_2 = sorted_arrays_overlap(array_2, array_1)
        actual_3 = sorted_arrays_overlap(array_1, array_1)
        expected = "Invalid input types! Both parameters should be arrays."
        self.assertEqual(actual_1, expected)
        self.assertEqual(actual_2, expected)
        self.assertEqual(actual_3, expected)

    #  Invalid input (1b): empty arrays
    def test_02_invalid_input_empty_arrays(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23, 34, 52]
        array_2 = []
        actual_1 = sorted_arrays_overlap(array_1, array_2)
        actual_2 = sorted_arrays_overlap(array_2, array_1)
        actual_3 = sorted_arrays_overlap(array_2, array_2)
        expected = "Empty arrays! Neither of the arrays can be empty."
        self.assertEqual(actual_1, expected)
        self.assertEqual(actual_2, expected)
        self.assertEqual(actual_3, expected)

    # Invalid input (1c): non-integer arrays
    def test_03_invalid_input_non_integers(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23, 34, 52]
        array_2 = ['1', '2', '5', '7', '8', '15', '19', '25', '34', '62']
        actual_1 = sorted_arrays_overlap(array_1, array_2)
        actual_2 = sorted_arrays_overlap(array_2, array_1)
        actual_3 = sorted_arrays_overlap(array_2, array_2)
        expected = "Invalid data types within arrays! Arrays should contain only integers."
        self.assertEqual(actual_1, expected)
        self.assertEqual(actual_2, expected)
        self.assertEqual(actual_3, expected)

    #  Invalid input (1d): not sorted arrays
    def test_04_invalid_input_not_sorted(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23, 34, 52]
        array_2 = [7, 34, 1, 8, 19, 15, 25, 62, 5, 2]
        actual_1 = sorted_arrays_overlap(array_1, array_2)
        actual_2 = sorted_arrays_overlap(array_2, array_1)
        actual_3 = sorted_arrays_overlap(array_2, array_2)
        expected = "Not sorted arrays! Both arrays should be sorted in ascending order."
        self.assertEqual(actual_1, expected)
        self.assertEqual(actual_2, expected)
        self.assertEqual(actual_3, expected)

    def _assert(self, array_1, array_2):
        try:
            actual = sorted_arrays_overlap(array_1, array_2)
            expected = self.sorted_arrays_overlap_test_class(array_1, array_2)
        except Exception:
            self.fail("An unexpected error is raised.")
        self.assertEqual(expected, actual)

    #  Corner case (2a): arrays with different length
    def test_05_different_length(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23]
        array_2 = [1, 2, 5, 7, 8, 15, 19, 25, 34, 62]
        self._assert(array_1, array_2)
        self._assert(array_2, array_1)

    #  Corner case (2b): arrays with duplicate elements
    def test_06_duplicates_in_arrays(self):
        array_1 = [1, 3, 3, 7, 8, 14, 19, 23, 23, 52]
        array_2 = [1, 2, 5, 7, 8, 15, 19, 25, 34, 62]
        array_3 = [1, 2, 5, 5, 8, 8, 19, 19, 34, 62]
        self._assert(array_1, array_2)
        self._assert(array_2, array_1)
        self._assert(array_1, array_3)  # Duplicates in both arrays

    #  Corner case (2c): arrays with same elements
    def test_07_same_elements(self):
        array_1 = [1, 3, 5, 7, 8, 14, 19, 23, 34, 52]
        array_2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        array_3 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self._assert(array_1, array_2)
        self._assert(array_2, array_1)
        self._assert(array_1, array_1)  # Arrays are equal, elements in the array are not the same
        self._assert(array_2, array_2)  # Each array has same elements, arrays are equal
        self._assert(array_2, array_3)  # Each array has same elements, they differ across arrays

    #  Corner case (2d): arrays with negative integers
    def test_08_negative_integers_in_arrays(self):
        array_1 = [1, 3, 3, 7, 8, 14, 19, 23, 23, 52]
        array_2 = [1, 2, 5, 7, 8, 15, 19, 25, 34, 62]
        array_3 = [-5, -3, -1, 7, 8, 14, 19, 23, 34, 52]
        array_4 = [-8, -7, -5, -2, -1, 15, 19, 25, 34, 62]
        self._assert(array_1, array_4)
        self._assert(array_2, array_3)
        self._assert(array_3, array_4)

    #  Corner case (2e): arrays with only 1 element NO FAULTY IMPLEMENTATION
    def test_09_only_one_element_in_arrays(self):
        array_1 = [1, 3, 3, 7, 8, 14, 19, 23, 23, 52]
        array_2 = [7]
        array_3 = [5]
        self._assert(array_1, array_2)
        self._assert(array_2, array_1)
        self._assert(array_2, array_3)

    #  Corner case (3a): arrays with no overlap
    def test_10_no_overlap(self):
        array_1 = [1, 3, 3, 7, 8, 14, 19, 23, 23, 52]
        array_2 = [25, 30, 35, 41, 47, 50, 56, 67, 80, 99]
        actual_1 = sorted_arrays_overlap(array_1, array_2)
        actual_2 = sorted_arrays_overlap(array_2, array_1)
        expected = "There are no overlapping elements in given arrays."
        self.assertEqual(actual_1, expected)
        self.assertEqual(actual_2, expected)

    #  Normal case (3b): arrays of positive integers with overlap
    def test_11_positive_integers_overlap(self):
        array_1 = [1, 3, 3, 7, 8, 14, 19, 23, 23, 52]
        array_2 = [3, 5, 7, 41, 47, 50, 52, 67, 80, 99]
        self._assert(array_1, array_2)
        self._assert(array_2, array_1)
