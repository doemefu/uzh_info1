from unittest import TestCase

class PublicTestSuite(TestCase):

    def test_floor(self):
        from task import script
        floor_value = script.zoo(5.7)[0]
        self.assertEqual(floor_value, 5)

