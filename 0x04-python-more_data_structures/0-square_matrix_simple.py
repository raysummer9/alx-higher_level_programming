#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nw_arry = []
    for lists in matrix:
        rslt = list(map(lambda x: x ** 2, lists))
        nw_arry.append(rslt)
    return nw_arry
