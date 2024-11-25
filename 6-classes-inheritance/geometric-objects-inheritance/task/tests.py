#!/usr/bin/env python3

from unittest import TestCase
from task.cube import Cube
from task.cone import Cone
from task.cylinder import Cylinder


class CubeTest(TestCase):
    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
    def test_cube_color(self):
        cube = Cube("red", True, 10)
        actual = cube.color
        self.assertEqual(actual, "red")

    def test_cone_color(self):
        cone = Cone("yellow", False, 10, 5, 6.4)
        actual = cone.color
        self.assertEqual(actual, "yellow")

    def test_cylinder_color(self):
        cylinder = Cylinder("blue", True, 3.5, 6.3)
        actual = cylinder.color
        self.assertEqual(actual, "blue")


