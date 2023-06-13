#!/usr/bin/python3
"""This module contains the class 'Student'"""
import json


class Student:
    """Class definition for 'Student' class"""
    def __init__(self, first_name, last_name, age):
        """Initialization function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that retrieves a dictionary representation
        of a 'Student' instance
        """
        return self.__dict__
