#!/usr/bin/python3
"""Find a peak module """


def find_peak(list_of_integers):
    """Find a peak function"""
    if len(list_of_integers) > 0:
        if len(list_of_integers) == 1:
            return list_of_integers[0]
        else:
            mid = len(list_of_integers) // 2
            peak = list_of_integers[mid]
            left = find_peak(list_of_integers[:mid])
            right = find_peak(list_of_integers[mid:])
            if left > peak:
                peak = left
            if right > peak:
                peak = right
            return peak
