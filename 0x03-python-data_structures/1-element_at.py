#!/usr/bin/python
def element_at(my_list, idx):
    list_size = len(my_list)
    if idx < 0 or idx >= list_size:
        return None
    else:
        return my_list[idx]
