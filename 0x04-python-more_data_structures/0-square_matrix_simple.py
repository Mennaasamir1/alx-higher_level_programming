#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_list = []
        new_list.append([[element ** 2 for element in row]
                    for row in matrix])
        return new_list
