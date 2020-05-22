#!/usr/bin/python3
def matrix_divided(matrix, div):
    """matrix_divided is a function that divides all elements of a matrix
    Args:
        matrix (list): list to operate
        div (int or float): number to operate

    Raises:
        TypeError: if matrix is not a list of lists of integers/float, or if
        each row of the matrix does not have the same size, or if div is not an
        integer or float

        ZeroDivisionError: if div is equal to 0
    """
    msgError_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    msgError_2 = 'Each row of the matrix must have the same size'
    var_1 = -1
    var_2 = 0
    new_m = []
    aux = []
    if type(matrix) != list:
        raise TypeError(msgError_1)
    var_2 = len(matrix)
    for x in matrix:
        aux = []
        if type(x) != list:
            raise TypeError(msgError_1)
        if var_1 == -1:
            var_1 = len(x)
        else:
            if var_1 != len(x):
                raise TypeError(msgError_2)
        for i in x:
            if type(i) not in [int, float]:
                raise TypeError(msgError_1)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for x in matrix:
        aux = []
        for i in x:
            aux.append(round(i / div, 2))
        new_m.append(aux)
    return new_m
