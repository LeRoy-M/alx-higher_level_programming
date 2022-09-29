#!/usr/bin/python3
"""This module creates a class"""


class Rectangle:
    """This class is based on the previous module (7-base_geometry.py)"""
    def __init__(self, width, height):
        """Initialization method"""
        self.__width = width
        self.__height = height

    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, width, height):
        """This method validates 'value'

        Args:
            width (int): Value passed for validation
            height (int): Value passed for validation
        """
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be greater than 0")
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be greater than 0")
