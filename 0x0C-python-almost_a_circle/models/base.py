#!/usr/bin/python3

"""Module class definition"""


class Base:
    """the base of all classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
