from unittest import TestCase
from task.script import evolve

demo = ("-----",
        "|   |",
        "| # |",
        "-----")

class SampleMoveTests(TestCase):
    def test_field_return_type(self):
        result, alive = evolve(demo, 1)
        self.assertEqual(type(result), tuple)

    def test_alive_return_type(self):
        result, alive = evolve(demo, 1)
        self.assertEqual(type(alive), int)

    def test_invalid_field_type_1(self):
        with self.assertRaises(Warning):
            evolve([], 1)

    def test_invalid_field_type_2(self):
        with self.assertRaises(Warning):
            evolve("what", 1)

    def test_invalid_steps_type_1(self):
        with self.assertRaises(Warning):
            evolve(demo, 1.0)

    def test_invalid_steps_type_2(self):
        with self.assertRaises(Warning):
            evolve(demo, "what")

    def test_invalid_empty_field0(self):
        with self.assertRaises(Warning):
            evolve((), 1)

    def test_invalid_empty_field1(self):
        with self.assertRaises(Warning):
            evolve(("",), 1)

    def test_invalid_empty_field2(self):
        with self.assertRaises(Warning):
            evolve(("", ""), 1)

    def test_invalid_small_field1(self):
        with self.assertRaises(Warning):
            evolve(("---", "---"), 1)

    def test_invalid_small_field2(self):
        with self.assertRaises(Warning):
            evolve(("--", "||", "--"), 1)

    def test_inconsisnten_dimensions(self):
        with self.assertRaises(Warning):
            evolve(("---", "||", "---"), 1)

    def test_invalid_invalid_cells(self):
        with self.assertRaises(Warning):
            evolve(("---", "|-|", "---"), 1)

    def test_invalid_invalid_frame_1(self):
        with self.assertRaises(Warning):
            evolve(("- -", "| |", "---"), 1)

    def test_invalid_invalid_frame_2(self):
        with self.assertRaises(Warning):
            evolve(("---", "|  ", "---"), 1)

    def test_provided_example(self):
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
        self.assertEqual(expected, actual)

    def test_still_lifes(self):
        field = (
            "--------------",
            "| ##    ##   |",
            "| ##   #  #  |",
            "|       ##   |",
            "|            |",
            "| ##         |",
            "| # #        |",
            "|  #         |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ##    ##   |",
            "| ##   #  #  |",
            "|       ##   |",
            "|            |",
            "| ##         |",
            "| # #        |",
            "|  #         |",
            "--------------"
        ), 15)
        actual = evolve(field, 50)
        self.assertEqual(expected, actual)

    def test_oscillators(self):
        field = (
            "-----------------",
            "| #             |",
            "| #   ###       |",
            "| #             |",
            "|               |",
            "|           ##  |",
            "|           ##  |",
            "|  #          ##|",
            "|#  #         ##|",
            "|#  #           |",
            "| #             |",
            "-----------------"
        )
        expected = ((
            "-----------------",
            "|      #        |",
            "|###   #        |",
            "|      #        |",
            "|               |",
            "|           ##  |",
            "|           #   |",
            "|              #|",
            "| ###         ##|",
            "|###            |",
            "|               |",
            "-----------------"
        ), 18)
        actual = evolve(field, 7)
        self.assertEqual(expected, actual)

