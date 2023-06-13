#!/usr/bin/python3
"""This module contains the 'class_to_json' function"""
import json


def class_to_json(obj):
    """Function that returns dict description with simple
    data structure for JSON serialization of an object
    """
    return json.loads(json.dumps(obj, default=lambda o : o.__dict__))
