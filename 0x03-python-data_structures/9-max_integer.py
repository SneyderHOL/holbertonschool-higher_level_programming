#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        idx = 0
        for i in range(len(my_list)):
            if (my_list[idx] < my_list[i]):
                idx = i
        return my_list[idx]
