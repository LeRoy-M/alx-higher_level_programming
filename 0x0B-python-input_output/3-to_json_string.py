#!/usr/bin/python3
"""This module contains the 'to_json_string' function"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation
    of an object
    """
    return json.dumps(my_obj)
