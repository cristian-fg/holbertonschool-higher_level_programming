#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    new = list(map(lambda x: x if x != search else replace, new))
    return new
