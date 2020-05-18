#!/usr/bin/python3
def safe_print_division(a, b):
    ret = 0
    try:
        ret = (a / b)
    except (ZeroDivisionError):
        ret = None
    finally:
        print('Inside result:', ret)
        return ret
