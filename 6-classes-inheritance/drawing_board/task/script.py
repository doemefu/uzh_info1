class MagicDrawingBoard:
    def __init__(self, spalten1, zeilen1):
        if spalten1 < 1 or zeilen1 < 1:
            raise ValueError("Board dimensions must be greater than 0")
        self.maxs = spalten1
        self.maxz = zeilen1
        self.temp_img = [[0] * spalten1 for _ in range(zeilen1)]

    def pixel(self, a):
        x, y = a
        if not (0 <= x < self.maxs and 0 <= y < self.maxz):
            raise ValueError("Coordinate out of bounds")
        self.temp_img[y][x] = 1

    def rect(self, a, b):
        x1, y1 = a
        x2, y2 = b
        if x1 >= x2 or y1 >= y2:
            raise ValueError("End coordinate must be greater than start coordinate")
        if not (0 <= x1 < self.maxs and 0 <= y1 < self.maxz) or not (0 <= x2 <= self.maxs and 0 <= y2 <= self.maxz):
            raise ValueError("Rectangle coordinates out of bounds")

        for y in range(y1, y2):
            for x in range(x1, x2):
                self.temp_img[y][x] = 1

    def img(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self.temp_img)

    def reset(self):
        self.temp_img = [[0] * self.maxs for _ in range(self.maxz)]


# Test cases to ensure functionality
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)  # instantiation of a specific size
    db.pixel((1, 1))  # draw at one coordinate
    db.rect((2, 2), (6, 4))  # draw a rectangle
    img = db.img()  # return the drawn image
    print(img)
    db.reset()  # reset the field again
