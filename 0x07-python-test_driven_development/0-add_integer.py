#!/usr/bin/python3
"""Containing functions"""


def add_integer(a, b=98):
    """Adds two integers"""
    # Validating data
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Casting any floats
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
