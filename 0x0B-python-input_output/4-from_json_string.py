#!/usr/bin/python3
"""This module contains the 'from_json_string' function"""
import json


def from_json_string(my_str):
    """Function that returns the JSON representation
    of an object
    """
    return json.loads(my_str)
