#!/usr/bin/env python3
from unittest import TestCase
from script import median

# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.
class MedianTests(TestCase):
    def test_def_1(self):
        self.assertEqual(2,median([1,2,3]))

    def test_def_2(self):
        self.assertEqual(2.5,median([1,2,3,4]))

    def test_user_4(self):
        self.assertEqual(None,median([]))