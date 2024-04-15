#!/usr/bin/python3

"""create a class MyList that inherits from list"""


class MyList(list):
    """sub-class of list"""
    def __init__(self):
        """init the object"""
        super().__init__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
