#!/usr/bin/python3

"""Text file function definition"""


def read_file(filename=""):
    """print the content stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
