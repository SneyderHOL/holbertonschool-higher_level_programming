#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    if my_list:
        if (x > my_list.__len__()):
            x = my_list.__len__()
        for i in range(x):
            try:
                print(my_list[i] * 1, end='')
            except TypeError:
                print('Element not an integer')
        else:
            print('')
        ret = i + 1
    return ret
