#!/usr/bin/python3
"""This module contains the 'Square' class and inherits
from 'Rectangle' in module '9-rectangle'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition for 'Square'"""
    def __init__(self, size):
        """Initialization method"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """String method"""
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        """Method to calculate area of a square"""
        return self.__size * self.__size
