#!/usr/bin/python3
"""This module contains the 'save_to_json_file' function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that returns the JSON representation
    of an object
    """
    with open(filename, mode="a", encoding="utf-8") as jf:
        jf.write(json.dumps(my_obj))
