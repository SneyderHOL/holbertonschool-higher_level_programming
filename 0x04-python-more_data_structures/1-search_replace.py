#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [] + my_list
    if new_list:
        while search in new_list:
            new_list[new_list.index(search)] = replace
    return new_list
