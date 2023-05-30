#!/usr/bin/python3
"""This module defines a class 'Square' based off of
the module '3-square'
"""


class Square:
    """The class 'Square' that has a private
    attribute
    """
    def __init__(self, size=0):
        """The class is initialized here"""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve 'size' field"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of an object variable 'size'"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of a square object and
        returns the value
        """
        return (self.__size * self.__size)
