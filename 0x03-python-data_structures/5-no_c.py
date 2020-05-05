#!/usr/bin/python3
def no_c(my_string):
    str = my_string
    if my_string:
        if 'c' in my_string or 'C' in my_string:
            str = ""
            for i in range(len(my_string)):
                c = my_string[i]
                if c != 'c' and c != 'C':
                    str += c
    return str
