#!/usr/bin/python3
"""This module creates a class"""


class BaseGeometry:
    """This class is based on the previous module (6-base_geometry.py)"""
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates 'value'"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
