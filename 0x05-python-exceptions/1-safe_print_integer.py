#!/usr/bin/python3
def safe_print_integer(value):
    ret = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        ret = False
    return ret
