#!/usr/bin/python3
import json
"""This module contains the 'to_json_string' function"""


def to_json_string(my_obj):
    """Function that returns the JSON representation
    of an object
    """
    return json.dumps(my_obj)
