#!/usr/bin/env python3
from unittest import TestCase
from script import sort

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class SortTests(TestCase):
    def test_input_1(self):
        self.assertEqual(None,sort(3))

    def test_input_2(self):
        self.assertEqual(None,sort(None))

    def test_input_3(self):
        self.assertEqual(list,type(sort([1,2])))

    def test_input_4(self):
        self.assertEqual(["a","b","c"], sort("bac"))

    def test_func_1(self):
        self.assertEqual([1,2,3], sort([1,2,3]))

    def test_func_2(self):
        self.assertEqual([1,2,3], sort([1,3,2]))