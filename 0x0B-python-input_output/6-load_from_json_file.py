#!/usr/bin/python3
"""This module contains the 'load_from_json_file' function"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a 'JSON file'"""
    with open(filename, mode="r", encoding="utf-8") as jf:
        return json.loads(jf.read())
