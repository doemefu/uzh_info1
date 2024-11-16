from unittest import TestCase

class PublicTestSuite(TestCase):

    def test_example(self):
        from task import script
        elements = (1, 2, 2, 3, 4, "Hi!", "Hi!") # lenth: 7
        actual_length = len(script.list_unique(elements))
        expected_length = 5
        self.assertEqual(expected_length, actual_length)

