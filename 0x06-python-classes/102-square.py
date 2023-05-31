#!/usr/bin/python3
"""This module defines a class 'Square' based off of
the module '4-square'
"""


class Square:
    """The class 'Square' that has a private
    attribute
    """
    def __init__(self, size=0):
        """The class is initialized here"""
        self.__size = size

    def __eq__(self, other):
        """Checks if the two class instances have
        the same area
        """
        if isinstance(other, Square):
            return (self.area() == other.area())

    def __ne__(self, other):
        """Checks that two class instances do NOT have
        the same area
        """
        if isinstance(other, Square):
            return (self.area() != other.area())

    def __gt__(self, other):
        """Checks if the first class instance has
        a greater area than the second one
        """
        if isinstance(other, Square):
            return (self.area() > other.area())

    def __ge__(self, other):
        """Checks if the first class instance has an
        equal or greater area than the second one
        """
        if isinstance(other, Square):
            return (self.area() >= other.area())

    def __lt__(self, other):
        """Checks if the first class instance has
        a lesser area than the second one
        """
        if isinstance(other, Square):
            return (self.area() < other.area())

    def __le__(self, other):
        """Checks if the first class instance has an
        equal or lesser area than the second one
        """
        if isinstance(other, Square):
            return (self.area() <= other.area())

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
