#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_list = [[element ** 2 for element in row] for row in matrix]
        return new_list
