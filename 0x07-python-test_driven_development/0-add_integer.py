#!/usr/bin/python3

"""Defination of of a function that adds two integers"""

def add_integer(a, b=98):
    """Checks if a and b are either integers or floats

    Casts a and b to integers if they are floats

    Raises:
            TypeError if either a or b is a non integer
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
