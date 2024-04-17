#!/usr/bin/python3

"""Define a function that returns the obj of an inherited class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is inherited or instance from a_class else False"""
    return (isinstance(obj, a_class))
