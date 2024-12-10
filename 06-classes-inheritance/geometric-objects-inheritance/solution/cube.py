from task.geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, color, filled, side_length):
        super().__init__(color, filled)
        self.side_length = side_length

    def area(self):
        area = 6 * pow(self.side_length, 2)
        return round(area, 2)

    def volume(self):
        volume = pow(self.side_length, 3)
        return round(volume, 2)
