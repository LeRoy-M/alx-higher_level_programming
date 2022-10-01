#!/usr/bin/python3
"""This module contains the add_attribute function
"""


def add_attribute(obj, attr, name):
    """This function adds a new attribute to an object if possible"""
    if ('__slots__' in dir(obj)) or '__dict__' not in dir(obj) or hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, name)
