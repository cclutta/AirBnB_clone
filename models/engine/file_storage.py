#!/usr/bin/python3
""" File storage module
"""
import json


class FileStorage:
    """That serializes instances to a JSON file and deserializes JSON. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key. """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file. """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects. """
        try:
            with open(FileStorage.__file_path, "r") as f:
                input = json.load(f)
                for k, v in input.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
        except IOError:
            pass
