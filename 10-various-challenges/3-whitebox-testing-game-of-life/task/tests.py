#!/usr/bin/env python3
from unittest import TestCase
from script import evolve


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `evolve` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class EvolveTestSuite(TestCase):

    def _assert_return_type(self, actual, expected):
        m = f"The evolve function should return a {type(expected)} but returned a {type(actual)}!"
        self.assertIsInstance(actual, type(expected), m)

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_input_tuple_1(self):
        with self.assertRaises(Warning):
            evolve(1, 4)

    def test_input_tuple_2(self):
        field = ("--------------",2)
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_char(self):
        s = '!"$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~üöäÜÖÄèéàÈÉÀ¨£'
        for x in s:
            field = (
                "--------------",
                f"|         {x}  |",
                "|  ###       |",
                "|  #         |",
                "|   #        |",
                "|            |",
                "--------------"
            )
            with self.assertRaises(Warning):
                evolve(field, 4)

    def test_input_length_1(self):
        field = (
            "-------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_length_2(self):
        field = (
            "--------------",
            "|           |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_length_3(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "-------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_size_1(self):
        field = (
            "--------------",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_size_2(self):
        field = (
            "--",
            "||",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_input_steps_1(self):
        field = (
            "--",
            "| |",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, 0)

    def test_input_steps_2(self):
        field = (
            "--",
            "| |",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, -1)

    def test_input_steps_3(self):
        field = (
            "--",
            "| |",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, "x")

    def test_game_mini(self):
        field = (
            "---",
            "|#|",
            "---"
        )
        expected = ((
            "---",
            "| |",
            "---"
        ), 0)
        actual = evolve(field, 4)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_game_2(self):
        field = (
            "--------------",
            "|            |",
            "|            |",
            "|    #       |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "--------------"
        ), 0)
        actual = evolve(field, 4)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_game_3(self):
        field = (
            "--------------",
            "|            |",
            "|            |",
            "|   ##       |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|            |",
            "|            |",
            "|   ##       |",
            "|   ##       |",
            "|            |",
            "--------------"
        ), 4)
        actual = evolve(field, 1)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_game_inf(self):
        field = (
            "--------------",
            "|            |",
            "|            |",
            "|   ##       |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|            |",
            "|            |",
            "|   ##       |",
            "|   ##       |",
            "|            |",
            "--------------"
        ), 4)
        actual = evolve(field, 30)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_game_4(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|   #        |",
            "|  ##        |",
            "|  # #       |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 1)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)

    def test_game_5(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self._assert_return_type(actual, expected)
        self.assertEqual(expected,actual)