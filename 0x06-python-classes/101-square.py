#!/usr/bin/python3
"""An other square for god sake"""


class Square():
    """The constructor function"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """The size retriever"""
    @property
    def size(self):
        return self.__size

    """The size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """The position retriever"""
    @property
    def position(self):
        return self.__position

    """The position mutator"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    """Calculates the square area"""
    def area(self):
        return self.__size * self.__size

    """Prints the square"""
    def my_print(self):
        if self.__position[1] > 0:
            [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)

    """Called on print function"""
    def __string__(self):
        string = ""
        self.my_print()
        return string
