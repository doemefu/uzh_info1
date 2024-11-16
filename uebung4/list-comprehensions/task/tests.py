#!/usr/bin/env python3
from unittest import TestCase
import task.script as script

class MyTestSuite(TestCase):

    def test_square_numbers(self):
        self.assertEqual(script.square_numbers([1, 2, 3]), [1, 4, 9])

    def test_only_integers(self):
        self.assertEqual(script.only_integers([1.1, 2]), [2])

    # Note that you can copy paste the function above and rewrite it to test
    # your other functions!

