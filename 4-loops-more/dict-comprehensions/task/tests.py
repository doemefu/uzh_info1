from unittest import TestCase
import task.script as script

class MyTestSuite(TestCase):

    def test_even_odd_length(self):
        numbers = [1, -1, 1]
        self.assertTrue(len(script.even_odd_dict(numbers)) == 2)

    # Note that you can copy paste the function above and rewrite it to test
    # your other functions!
