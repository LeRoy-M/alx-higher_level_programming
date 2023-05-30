#!/usr/bin/python3
"""This module defines a class 'Square' based off of
the module '1-square'
"""


class Square:
    """The class 'Square' that has a private
    attribute
    """
    def __init__(self, size=0):
        """The class is initialized here, with
        'size' attribute
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
