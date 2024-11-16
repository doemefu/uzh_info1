#!/usr/bin/env python3
from unittest import TestCase
from script import sorted_arrays_overlap

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.


class SortedArraysOverlapTest(TestCase):
    def test_input_1(self):
        self.assertEqual("Invalid input types! Both parameters should be arrays.", sorted_arrays_overlap("str",1))

    def test_input_2(self):
        self.assertEqual("Invalid input types! Both parameters should be arrays.", sorted_arrays_overlap([1], 1))

    def test_input_3(self):
        self.assertEqual("Invalid input types! Both parameters should be arrays.", sorted_arrays_overlap(1,[1]))

    def test_empty_list_1(self):
        self.assertEqual("Empty arrays! Neither of the arrays can be empty.", sorted_arrays_overlap([],[1]))

    def test_empty_list_2(self):
        self.assertEqual("Empty arrays! Neither of the arrays can be empty.", sorted_arrays_overlap([1],[]))

    def test_empty_list_3(self):
        self.assertEqual("Empty arrays! Neither of the arrays can be empty.", sorted_arrays_overlap([],[]))

    def test_list_values_1(self):
        self.assertEqual("Invalid data types within arrays! Arrays should contain only integers.", sorted_arrays_overlap(["str"],[1]))

    def test_list_values_2(self):
        self.assertEqual("Invalid data types within arrays! Arrays should contain only integers.", sorted_arrays_overlap([1],["str"]))

    def test_list_values_3(self):
        self.assertEqual("Invalid data types within arrays! Arrays should contain only integers.", sorted_arrays_overlap([1,"str"],[1]))

    def test_list_sorted_1(self):
        self.assertEqual("Not sorted arrays! Both arrays should be sorted in ascending order.", sorted_arrays_overlap([1,2],[2,1]))

    def test_list_sorted_2(self):
        self.assertEqual("Not sorted arrays! Both arrays should be sorted in ascending order.", sorted_arrays_overlap([3,1,2],[1,2]))

    def test_check_overlap_1(self):
        self.assertEqual("There are no overlapping elements in given arrays.", sorted_arrays_overlap([1],[2]))

    def test_check_overlap_2(self):
        self.assertEqual("There are no overlapping elements in given arrays.", sorted_arrays_overlap([1,3],[2,4]))

    def test_check_overlap_3(self):
        self.assertEqual([1],sorted_arrays_overlap([1],[1,2]))

    def test_check_overlap_4(self):
        self.assertEqual([6,7,8,9],sorted_arrays_overlap([5,6,7,8,9],[6,7,8,9,10]))

    def test_check_overlap_5(self):
        self.assertEqual([6,6,8,9],sorted_arrays_overlap([5,6,6,8,9],[6,6,8,9,10]))

    def test_negative_1(self):
        self.assertEqual([-2, -1],sorted_arrays_overlap([-3,-2,-1],[-2,-1,0]))

    def test_negative_2(self):
        self.assertEqual([-2, -1,1,2],sorted_arrays_overlap([-3,-2,-1,1,2],[-2,-1,0,1,2]))