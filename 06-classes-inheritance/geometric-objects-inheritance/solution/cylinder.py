from task.geometric_object import GeometricObject
from math import pi


class Cylinder(GeometricObject):
    def __init__(self, color, filled, radius, height, ):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def area(self):
        area = (
            2 * pi * pow(self.radius, 2)
            + 2 * pi * self.radius * self.height
        )
        return round(area, 2)

    def volume(self):
        volume = pi * pow(self.radius, 2) * self.height
        return round(volume, 2)
