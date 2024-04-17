#!/usr/bin/python3

"""a class Student that defines a student"""


class Student:
    """Create a Student instance"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dictionary representation of a Student"""
        return self.__dict__.copy()
