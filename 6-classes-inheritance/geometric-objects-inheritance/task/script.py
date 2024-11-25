#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from cone import Cone
from cube import Cube

# Create first cone object
cone_1 = Cone("red", True, 2, 4, 2)

# Create another cone object
cone_2 = Cone("black", False, 5.64, 4.2, 8.7)

# Create a cube object
cube = Cube("white", True, 7.2)
print(f"Color of the cube object is: {cube.color}")

# Update cube color
cube.color = "yellow"

# See if the color of cube object is changed
print(f"Color of the cube object is: {cube.color}")

# See the area and volume of the cone_1
print(f"cone_1 area is: {cone_1.area()} cone_2 volume is: {cone_1.volume()}")

