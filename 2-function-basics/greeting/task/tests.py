from unittest import TestCase

from task import script

class TestSuite(TestCase):

    def test_alice_45(self):
        actual = script.generate_greeting("Alice", 45)
        expected = f"Hello Alice, you are 45 years old!"
        self.assertEqual(expected, actual)

