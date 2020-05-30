#!/usr/bin/python3
"""
Module that multiplies two matrices using the module NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """matrix_mul is a function that multiplies two matrices
    Args:
        m_a (list): matrix to operate
        m_b (list): matrix to operate
    Raises:
        TypeError: if matrix is not a list or if is not a list of lists, or if
        matrix have any element different than integers/float, or if each row
        of the matrix do not have the same size

        ValueError: if matrix is empty, or if m_a and m_b can't be multiplied
    """
    msgError = "m_a and m_b can't be multiplied"
    new_m = []
    matrix_check(m_a, 'm_a')
    matrix_check(m_b, 'm_b')
    if len(m_a[0]) != len(m_b):
        raise ValueError(msgError)
    new_m = np.matmul(np.array(m_a), np.array(m_b))
    return new_m


def matrix_check(matrix, matrix_name):
    """matrix_check is a function that check if a matrix is valid for
        multiplication
    Args:
        matrix (list): matrix to validate
        matrix_name (string): name of matrix to print in case of error
    Raises:
        TypeError: if matrix is not a list or if is not a list of lists, or if
        matrix have any element different than integers/float, or if each row
        of the matrix do not have the same size

        ValueError: if matrix is empty
    """
    msgError_1 = ' must be a list'
    msgError_2 = ' must be a list of lists'
    msgError_3 = ' can\'t be empty'
    msgError_4 = ' should contain only integers or floats'
    msgError_5 = 'each row of '
    msgError_6 = ' must be of the same size'
    var_1 = 0
    if type(matrix) != list:
        raise TypeError(matrix_name + msgError_1)
    if not matrix:
        raise ValueError(matrix_name + msgError_3)
    if len(matrix) == 1:
        if not matrix[0]:
            raise ValueError(matrix_name + msgError_3)
    for x in matrix:
        if type(x) != list:
            raise TypeError(matrix_name + msgError_2)
        if var_1 == 0:
            var_1 = len(x)
        else:
            if var_1 != len(x):
                raise TypeError(msgError_5 + matrix_name + msgError_6)
        for i in x:
            if type(i) not in [int, float]:
                raise TypeError(matrix_name + msgError_4)
