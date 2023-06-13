#!/usr/bin/python3
"""This module contains the 'class_to_json' function"""
import json


def class_to_json(obj):
    """Function that returns dict description with simple
    data structure for JSON serialization of an object
    """
    return obj.__dict__
