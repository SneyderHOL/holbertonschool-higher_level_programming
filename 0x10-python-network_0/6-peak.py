#!/usr/bin/python3
"""Find a peak module """


def find_peak(list_of_integers):
    """Find a peak function"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
