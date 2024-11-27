#!/usr/bin/env python3
from unittest import TestCase
import task.script as script

class MyTestSuite(TestCase):

    def test_words_containing_string(self):
        self.assertTrue(len(script.words_containing_string("pp")) == 3) # apple, pineapple and sapphire

    # Note that you can copy paste the function above and rewrite it to test
    # your other functions!

