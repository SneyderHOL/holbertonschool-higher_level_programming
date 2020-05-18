#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ret = True
    try:
        print('{:d}'.format(value))
    except ValueError as ve:
        print('Exception: {}'.format(ve), file=sys.stderr)
        ret = False
    return ret
