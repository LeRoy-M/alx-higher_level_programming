#!/usr/bin/python3
"""This module defines a class 'Square' based off of
the module '2-square'
"""


class Square:
    """The class 'Square' that has a private
    attribute
    """
    def __init__(self, size=0):
        """The class is initialized here, with
        an instance variable 'size'
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of a square object and
        returns the value
        """
        return (self.__size * self.__size)
