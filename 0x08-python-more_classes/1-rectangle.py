#!/usr/bin/python3
"""This module defines the class 'Rectangle' based on module '0-rectangle'"""


class Rectangle:
    """Defines a class 'Rectangle'"""
    def __init__(self, width=0, height=0):
        """Intializes 'Rectangle' instance with optional width and
        height fields set to '0'
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Function to retrieve private instance attribute 'width'"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Function to set private instance attribute 'width'"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def height(self):
        """Function to retrieve private instance attribute 'height'"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Function to set private instance attribute 'height'"""
        if (isinstance(value, int)):
            if (value > 0):
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
