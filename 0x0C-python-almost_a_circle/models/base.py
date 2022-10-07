#!/usr/bin/python3
"""This module creates the class 'base'"""


__nb_objects = 0

class Base:
    """This class defines the base program"""
    def __init__(self, id=None):
        """Intialization method

        Args:
            id (int): Object I.D
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
