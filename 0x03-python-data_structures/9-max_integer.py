#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    num = 0
    for i in range(len(my_list)):
        tmp = my_list[i]
        if (num < tmp):
            num = tmp
    return num
