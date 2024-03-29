#!/usr/bin/python3
"""A module about a square mob"""


class Square:
    """constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if (isinstance(position, tuple) and
                len(position) == 2 and
                all(isinstance(num, int) for num in position) and
                all(num >= 0 for num in position)):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Returns the square area"""
    def area(self):
        return self.__size * self.__size

    """Prints the square"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end='') for _ in range(self.__position[0])]
            [print("#", end='') for _ in range(self.__size)]
            print("")
