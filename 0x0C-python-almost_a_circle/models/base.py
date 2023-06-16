#!/usr/bin/python3
"""This module contains the 'Base' class"""


class Base:
    """Class `Base` declared and defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
