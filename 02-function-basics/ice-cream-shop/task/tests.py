from unittest import TestCase

class PublicTestSuite(TestCase):

    def test_example(self):
        from task import script
        actual = script.get_price(0.70, 1.00, 1.10, 1, 3)
        expected = 4.8
        self.assertAlmostEqual(expected, actual, 5)

