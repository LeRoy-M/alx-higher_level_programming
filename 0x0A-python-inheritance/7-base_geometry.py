#!/usr/bin/python3
"""This module contains the 'BaseGeometry' class based
on the '6-base_geometry' module
"""


class BaseGeometry:
    """Class definition for 'BaseGeometry'"""
    def area(self):
        """Method for area calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates 'value'"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
