#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ret = False
    try:
        print('{:d}'.format(value))
        ret = True
    except ValueError as ve:
        print('Exception: {}'.format(ve), file=sys.stderr)
    except TypeError as te:
        print('Exception: {}'.format(te), file=sys.stderr)
    return ret
