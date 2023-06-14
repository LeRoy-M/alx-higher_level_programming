#!/usr/bin/python3
"""This module contains the 'Rectangle' class based
on the '7-base_geometry' module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition for 'Rectangle'"""
    def __init__(self, width, height):
        """Initialization method"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
