#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    for i in range(len(my_list_1)):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
        finally:
            new_list = new_list + [res]
            res = 0
    while len(new_list) < list_length:
        new_list = new_list + [0]
    return new_list
