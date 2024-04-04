#!/usr/bin/python3
"""define a square"""


class Square:
    """represent square"""

    def __init__(self, size=0):
        """init a new square

        args:
            size(int): size of new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the are of the square we currently have"""
        return (self.__size * self.__size)
