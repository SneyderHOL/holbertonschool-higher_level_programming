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
    """
    return np.matmul(np.array(m_a), np.array(m_b))
