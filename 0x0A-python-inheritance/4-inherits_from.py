#!/usr/bin/python3

"""Inherited class function"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance inherited from a specific class"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
