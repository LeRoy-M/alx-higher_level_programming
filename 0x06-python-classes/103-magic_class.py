#!/usr/bin/python3
"""This module defines a class called 'MagicClass'
"""
import math


class MagicClass:
    """This is a MagicClass"""
    def __init__(self, radius=0):
        """The initialization function"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This method returns the area of a circle"""
        return (self.__radius**2*math.pi)

    def circumference(self):
        """This method returns the circumference of a circle"""
        return (2*math.pi*self.__radius)
