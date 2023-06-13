#!/usr/bin/python3
"""This module adds all arguments to a Python list, and
then save them to a file
"""
from sys import argv
from os import path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
cli_args = []

if len(argv) > 1:
    for i in range(len(argv) - 1):
        cli_args.append(argv[i + 1])

if path.isfile(filename):
    former_list = load_from_json_file(filename)
    former_list.extend(cli_args)
    cli_args = former_list

save_to_json_file(cli_args, filename)
