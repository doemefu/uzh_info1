from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, color, filled, side_length):
        super().__init__(color,filled)
        self.side_length =  side_length

    def area(self):
        return 6*(self.side_length**3)

    def volume(self):
        return self.side_length**3
