#!/usr/bin/python3
"""A module about a square mob"""


class Square:
    """constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Size getter"""
    @property
    def size(self):
        return self.__size

    """Size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Position getter"""
    @property
    def position(self):
        return self.__position

    """Position setter"""
    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) < 2 or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Returns the square area"""
    def area(self):
        return self.__size * self.__size

    """Prints the square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                if self.__position[1] == 0:
                    print(" " * self.__position[0], end='')
                print("#" * self.__size, end='')
                print()
