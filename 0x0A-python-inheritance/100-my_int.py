#!/usr/bin/python3
"""This module creates a class 'MyInt' that inherits from 'int'

    Args:
        int (_type_): Class parameter
"""


class MyInt(int):
    """This class inverts the 'boolean' operation return value"""
    def __ne__(self, other):
        """Method nverted 'boolean' output"""
        return super().__eq__(other)

    def __eq__(self, other):
        """Method nverted 'boolean' output"""
        return super().__ne__(other)
