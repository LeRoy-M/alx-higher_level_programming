#!/usr/bin/python3
"""This module contains the class 'Student' based on
module '9-student'
"""


class Student:
    """Class definition for 'Student' class"""
    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a 'Student' instance
        """
        if isinstance(attrs, list):
            new_dict = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    new_dict[item] = self.__dict__[item]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of the
        'Student' instance
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
