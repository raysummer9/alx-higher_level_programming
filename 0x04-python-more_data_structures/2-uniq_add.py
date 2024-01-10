#!/usr/bin/python3

def uniq_add(my_list=[]):
    values = set()
    for i in my_list:
        values.add(i)
    result = sum(values)
    return result
