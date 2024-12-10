#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise ValueError("Board is too small, positive dimensions required.")
        self.__x = x
        self.__y = y
        self.reset()

    def reset(self):
        self.__board = self.__x * self.__y * [0]

    def _idx(self, xy):
        x, y = xy
        return y*self.__x + x

    def _assert_coords(self, xy, is_end=False):
        x, y = xy
        if x<0 or y<0 or x>self.__x or y>self.__y:
            raise ValueError("Coordinates point outside of the board.")
        if not is_end:
            if x == self.__x or y == self.__y:
                raise ValueError("Only the endpoint of a rectangle can use coordinates that are outside the board.")

    def pixel(self, xy):
        self._assert_coords(xy)
        idx = self._idx(xy)
        self.__board[idx] = 1

    def rect(self, start_xy, end_xy):
        self._assert_coords(start_xy)
        self._assert_coords(end_xy, True)

        width = end_xy[0] - start_xy[0]
        height = end_xy[1] - start_xy[1]
        if width < 1 or height < 1:
            raise ValueError("Width and height of a rectangle must be greater than 0.")

        idx = self._idx(start_xy)
        for delta_x in range(width):
            for delta_y in range(height):
                cur = idx + delta_x + delta_y*self.__x
                self.__board[cur] = 1

    def img(self):
        s = ""
        for idx, v in enumerate(self.__board):
            if idx>0 and idx % self.__x == 0:
                s+="\n"
            s += "1" if v else "0"
        return s
