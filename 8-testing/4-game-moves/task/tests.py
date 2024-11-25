#!/usr/bin/env python3
from unittest import TestCase
from script import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_init_right(self):
        state = (
            "#####   #",
            "###    # ",
            "#   o ## ",
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   #",
                "###    # ",
                "#    o## ",
            ),
            ("left", "up")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_init_player_0(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_player_2(self):
        state = (
            "#####   ",
            "###  o #",
            "#  o  ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_char_1(self):
        state = (
            "##### y ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_char_all(self):
        s = '!"$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnpqrstuvwxyz{|}~üöäÜÖÄèéàÈÉÀ¨£'
        for x in s:
            state = (
                "#####   ",
                f"###   {x}#",
                "#  o  ##",
                "    ####"
            )
            with self.assertRaises(Warning):
                move(state, "up")

    def test_init_char_3(self):
        state = (
            "##### \" ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_line_1(self):
        state = (
            "#####   #", #too long
            "###  o #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_line_2(self):
        state = (
            "#####   ",
            "###  o #",
            "#     ###",#too long
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_line_3(self):
        state = (
            "#####   ",#too short
            "###    ##",
            "#  o  ###",
            "   ######"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_size0_1(self):
        state = (
            "",
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_size0_2(self):
        state = (
            " ",
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_size0_3(self):
        state = (
            "",
            "",
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_moves_tl(self):
        state = (
            "o####   ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_moves_br(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "   ####o"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_moves_0(self):
        state = (
            "#####   ",
            "#o#    #",
            "##    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_init_moves_1(self):
        state = (
            "#####   ",
            "##o    #",
            "##    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")
