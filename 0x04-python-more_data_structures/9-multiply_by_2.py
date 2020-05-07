#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    if a_dictionary:
        for k, v in a_dictionary.items():
            new[k] = v * 2
    return new
