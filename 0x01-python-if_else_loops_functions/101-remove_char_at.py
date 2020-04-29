#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        c = str[i]
        if i != n:
            new_str = new_str + c
    return new_str
