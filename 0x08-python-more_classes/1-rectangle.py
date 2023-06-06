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
        try:
            if (int(value) > 0):
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        except TypeError:
            print("width must be an integer")

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
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
