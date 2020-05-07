#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sort_keys = sorted(a_dictionary)
        for k in sort_keys:
            print("{} : {}".format(k, a_dictionary[k]))
