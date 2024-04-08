#!/usr/bin/python3
"""defining a Rectangle class"""


class Rectangle:
    """represent a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializing rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """get the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return the representation of the rectangle"""
        if self.__width == 0 and self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
            return ("".join(rec))
