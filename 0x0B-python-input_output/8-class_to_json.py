#!/usr/bin/python3
""" a function that returns the dictionary description"""
def class_to_json(obj):
    """return the dictionary of a simple data structure"""
    return obj.__dict__
