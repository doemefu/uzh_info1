#!/usr/bin/env python3

from unittest import TestCase
from task.script import sort


class SampleSortTests(TestCase):

    def test_sorting_works_list(self):
        actual = sort([3, 1, 2])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_sorting_works_tuple(self):
        actual = sort((3, 1, 2))
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_sorting_works_string(self):
        actual = sort(["c", "b", "a"])
        expected = ["a", "b", "c"]
        self.assertEqual(expected, actual)

    def test_sorting_works_int(self):
        actual = sort([3, 1, 2])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_sorting_works_float(self):
        actual = sort([3.0, 1.0, 2.0])
        expected = [1.0, 2.0, 3.0]
        self.assertEqual(expected, actual)

    def test_sorting_works_single_element(self):
        actual = sort([1])
        expected = [1]
        self.assertEqual(expected, actual)

    def test_none_is_caught(self):
        actual = sort(None)
        self.assertIsNone(actual)

    def test_non_iterable(self):
        actual = sort(1)
        self.assertIsNone(actual)

    def test_original_is_not_mutated(self):
        _in = [3, 1, 2]
        sort(_in)
        self.assertEqual([3, 1, 2], _in)

    def test_function_return_new_list_general(self):
        _in = [3, 1, 2]
        _out = sort(_in)
        self.assertIsNot(_in, _out)

    def test_function_return_new_list_empty(self):
        _in = []
        _out = sort(_in)
        self.assertIsNot(_in, _out)

    def test_function_return_new_list_single_element(self):
        _in = [1]
        _out = sort(_in)
        self.assertIsNot(_in, _out)
