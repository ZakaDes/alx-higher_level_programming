#!/usr/bin/python3

"""define class-checking function"""


def is_same_class(obj, a_class):
    """return True if object is the exact class as a_class, otherwise False"""
    return (type(obj) is a_class)
