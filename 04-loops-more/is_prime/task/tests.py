#!/usr/bin/env python3
from unittest import TestCase

from task import script


class PublicTestSuite(TestCase):
    def test_case0(self):
        m = "Incorrect for 3!"
        self.assertEqual("3 is prime", script.is_prime(3), m)

    def test_case1(self):
        m = "Incorrect for 12!"
        self.assertEqual(
            "12 is not a prime number (2 * 6 = 12)", script.is_prime(12), m
        )
