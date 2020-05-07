#!/usr/bin/python3
def weight_average(my_list=[]):
    num, den = 0, 0
    if my_list:
        for x in my_list:
            num += x[0] * x[1]
            den += x[1]
    return num / den
