#!/usr/bin/env python3
from unittest import TestCase
import script as script

class MyTestSuite(TestCase):

    def test_basic_scenario(self):
        employees = [
            ('Alice', 'Engineering', 70000),
            ('Bob', 'HR', 50000),
            ('Charlie', 'Engineering', 80000),
            ('David', 'Sales', 45000),
            ('Eve', 'HR', 52000)
        ]
        expected = {
            'Engineering': {'Alice': 70000, 'Charlie': 80000},
            'HR': {'Bob': 50000, 'Eve': 52000},
            'Sales': {'David': 45000}
        }
        actual = script.organize_employee_data(employees)
        self.assertEqual(expected, actual)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
