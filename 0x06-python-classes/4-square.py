#!/usr/bin/python3
"""A module that contains a square class"""


class Square:

    "object instantiator"
    def __init__(self, size=0):
        self.__size = size

    """Size retriever"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Returns the area of a square instance"""
    def area(self):
        return self.__size * self.__size
