#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = []
    if a_dictionary:
        for x in a_dictionary.items():
            if value in x:
                new_dict.append(x[0])
        for z in new_dict:
            del(a_dictionary[z])
    return a_dictionary
