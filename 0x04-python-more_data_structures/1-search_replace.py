#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nw_list = my_list[:]
    for i in nw_list:
        if i == search:
            index_replace = nw_list.index(search)
            nw_list[index_replace] = replace

    return nw_list
