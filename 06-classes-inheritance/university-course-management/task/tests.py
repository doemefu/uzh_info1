#!/usr/bin/env python3

from unittest import TestCase
from student import Student
from professor import Professor


class TestCars(TestCase):

    def test_get_details_student(self):
        student = Student("Alice", "alice@uzh.ch", "24-000-001")
        self.assertEqual(('Alice', 'alice@uzh.ch', '24-000-001'), student.get_details())

    def test_get_details_professor(self):
        professor = Professor("Dr. Dave", "dave@uzh.ch", "01234567", "BIN-0.Z.00")
        self.assertEqual(('Dr. Dave', 'dave@uzh.ch', '01234567', 'BIN-0.Z.00'), professor.get_details())

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
