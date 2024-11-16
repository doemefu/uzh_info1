from geometric_object import GeometricObject
from math import pi

class Cylinder(GeometricObject):
    def __init__(self, color, filled, radius, height):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def area(self):
        return 2*pi*(self.radius**2) + 2*pi*self.radius*self.height

    def volume(self):
        return pi*(self.radius**2)*self.height
