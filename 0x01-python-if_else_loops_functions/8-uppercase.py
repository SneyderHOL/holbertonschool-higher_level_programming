#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        new_str = new_str + c
    else:
        print("{}".format(new_str))
