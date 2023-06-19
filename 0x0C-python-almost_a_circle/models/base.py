#!/usr/bin/python3
"""This module contains the 'Base' class"""
import json
from os import path
import csv
import turtle


class Base:
    """Class `Base` declared and defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to convert objects to JSON string representation"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes JSON string representation of objects
        to a file
        """
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(cls.to_dictionary(obj))
        json_str = cls.to_json_string(list_dicts)
        with open(f'{cls.__name__}.json', mode='w', encoding='utf-8') as po:
            po.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Static method to convert JSON string representation to objects"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attirbutes
        already set
        """
        temp_inst = cls(1, 1)
        temp_inst.update(**dictionary)
        return temp_inst

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        objs = []
        if not path.isfile(f'{cls.__name__}.json'):
            return objs
        with open(f'{cls.__name__}.json', mode='r', encoding='utf-8') as js:
            list_dicts = cls.from_json_string(js.read())
            for dict_item in list_dicts:
                objs.append(cls.create(**dict_item))
            return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that writes JSON string representation of objects
        to a csv file
        """
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(cls.to_dictionary(obj))
        with open(f'{cls.__name__}.csv', mode='w') as po:
            field_names = list(list_dicts[0])
            writer = csv.DictWriter(po, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Class method that returns a list of instances from csv file"""
        objs = []
        if not path.isfile(f'{cls.__name__}.csv'):
            return objs
        with open(f'{cls.__name__}.csv', mode='r', newline='') as cf:
            reader = csv.reader(cf)
            header = next(reader)
            list_dicts = []
            for row in reader:
                obj_dict = {}
                for r in range(len(row)):
                    obj_dict[header[r]] = int(row[r])
                list_dicts.append(obj_dict)
            for dict_item in list_dicts:
                objs.append(cls.create(**dict_item))
            return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method that opens a window and draws all the
        'Rectangles' and 'Squares'
        """
        colors = ['cyan', 'yellow', 'magenta', 'white']
        while True:
            t = turtle.Turtle()
            turtle.bgcolor('black')
            t.speed(1)
            for i in range(200):
                t.pencolor(colors[i % 4])
                t.width(i / 100 + 1)
                t.right(90)
                t.forward(i)
