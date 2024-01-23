#!/usr/bin/python3
"""Defining a square again"""


class Square:
    """Defining a square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Returns the area of a square instance"""
    def area(self):
        return self.__size * self.__size
