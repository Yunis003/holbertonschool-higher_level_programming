#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    res = [list(map(lambda x: x ** 2, row)) for row in new_matrix]
    return res
