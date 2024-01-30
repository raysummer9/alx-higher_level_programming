#!/usr/bin/python3

"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): Matrix of integers and floats.
    div (int or float): Divisor.

    Returns:
    list of lists: New Matrix with elements divided by div

    Raises:
    TypeError: If matrix is not a list of ints or floats
                if each row of the matrix does not have the same size,
                or if div is not a number (integer or float).
    ZeroDivisionError: if div is equal to 0
    """

    if not all(isinstance(row, list) and all(isinstance(element, (int, float))for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
