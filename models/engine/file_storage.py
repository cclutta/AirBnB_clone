#!/usr/bin/python3
""" File storage module
"""
import json

from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """That serializes instances to a JSON file and deserializes JSON.
    Attributes:
        __file_path: file path
        __objects: object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key.
        Args:
            obj: object to set
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file. """
        obj_dict = FileStorage.__objects.copy()
        output = {k: v.to_dict() for k, v in obj_dict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(output, f, sort_keys=True, indent=4)

    def reload(self):
        """ deserializes the JSON file to __objects. """
        try:
            with open(FileStorage.__file_path, "r") as f:
                input = json.load(f)
                for k, v in input.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
        except Exception:
            pass
