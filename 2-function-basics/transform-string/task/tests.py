from unittest import TestCase

from task import script

class PublicTestSuite(TestCase):

    def test_example(self):
        actual = script.transform_string("aB:cD")
        expected = "ab:CD"
        self.assertEqual(expected, actual)

