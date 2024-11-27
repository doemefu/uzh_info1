#!/usr/bin/env python3

class Matrix:
    def __init__(self, in_matrix):
        assert type(in_matrix)==list
        assert len(in_matrix) > 0
        assert type(in_matrix[0]) == list

        the_len = len(in_matrix[0])
        for i in range(len(in_matrix)):
            assert type(in_matrix[i]) == list
            assert len(in_matrix[i]) > 0
            assert len(in_matrix[i]) == the_len

            for e in in_matrix[i]:
                assert type(e) == int

        self.__matrix = in_matrix

    def get_matrix(self):
        return self.__matrix.copy()

    # Also, implement the special methods __eq__, __hash__, __add__, and __mul__
    # as per the task description.

    def __add__(self, other):
        in_matrix = other.get_matrix()

        assert len(self.__matrix) == len(in_matrix) and len(self.__matrix[0]) == len(in_matrix[0])

        out_matrix = []
        for a in range(len(self.__matrix)):
            out_matrix.append([])
            for b in range(len(self.__matrix[a])):
                out_matrix[a].append( self.__matrix[a][b] + in_matrix[a][b])
        return Matrix(out_matrix)

    def __mul__(self, other):
        in_matrix = other.get_matrix()
        out_matrix = []

        z1 = len(self.__matrix)  #m
        s1 = len(self.__matrix[0]) #n
        z2= len(in_matrix)
        s2 = len(in_matrix[0]) #p

        assert s1 == z2

        for z in range(z1):
            out_matrix.append([])
            for s in range(s2):
                q = 0
                for x in range(s1):
                    q = q + self.__matrix[z][x] * in_matrix[x][s]
                out_matrix[z].append(q)

        return Matrix(out_matrix)


    def __eq__(self, other):
        in_matrix = other.get_matrix()
        assert len(self.__matrix) == len(in_matrix) and len(self.__matrix[0]) == len(in_matrix[0])

        for a in range(len(self.__matrix)):
            for b in range(len(self.__matrix[a])):
                if self.__matrix[a][b] != in_matrix[a][b]:
                    return False

        return True

    def __hash__(self):
        return hash(tuple([tuple(a) for a in self.__matrix]))
        #return tuple(self.__matrix).__hash__()

    def __repr__(self):
        return f"Matrix({self.__matrix})"

    def __str__(self):
        return f"Matrix({self.__matrix})"

# Make sure to work on task/tests.py as well to test your implementation!


if __name__ == '__main__':
    mc = Matrix([[7],[5],[6],[7]])

    ma = Matrix(
        [[1, 2],
         [3, 4]])

    mb = Matrix(
        [[1, 2],
         [3, 4]])

    print(ma==mb)
    print(ma+mb) #[[2, 4], [6, 8]]

    print(ma*mb) #[[7,10],[15,22]]

    print(hash(ma))