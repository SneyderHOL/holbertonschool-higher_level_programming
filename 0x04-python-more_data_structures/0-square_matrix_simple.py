#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for mat in matrix:
            new_matrix.append(list(map(lambda x: x ** 2, mat)))
    return new_matrix
