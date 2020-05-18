#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ret = None
    try:
        ret = fct(*args)
    except ZeroDivisionError as zde:
        print('Exception: {}'.format(zde), file=sys.stderr)
    except IndexError as ie:
        print('Exception: {}'.format(ie), file=sys.stderr)
    except ValueError as ve:
        print('Exception: {}'.format(ve), file=sys.stderr)
    except TypeError as te:
        print('Exception: {}'.format(te), file=sys.stderr)
    return ret
