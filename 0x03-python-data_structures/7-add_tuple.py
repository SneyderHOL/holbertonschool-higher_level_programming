#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a
    tuple_2 = tuple_b
    if (len(tuple_1) < 2):
        if len(tuple_1) == 1:
            tuple_1 = tuple_1[0], 0
        else:
            tuple_1 = 0, 0
    if (len(tuple_2) < 2):
        if len(tuple_2) == 1:
            tuple_2 = tuple_2[0], 0
        else:
            tuple_2 = 0, 0
    return tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
