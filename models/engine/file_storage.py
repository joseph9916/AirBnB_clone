#!/usr/bin/python3
"""
Writes the python object to a file by serialisng it as a Json String
"""


import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    """
    stores python objects to json stringed serialised files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialise __objects to the JSON file (path: __file_path)"""
        dictionary = dict(self.__objects)
        for key in dictionary:
            dictionary[key] = dictionary[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_string = f.read()
                objects = json.loads(json_string)
                for key in objects.keys():
                    cls = (objects[key])["__class__"]
                    if cls == "BaseModel":
                        obj = BaseModel(**objects[key])
                    if cls == "User":
                        obj = User(**objects[key])
                    if cls == "City":
                        obj = City(**objects[key])
                    if cls == "State":
                        obj = State(**objects[key])
                    if cls == "Place":
                        obj = Place(**objects[key])
                    if cls == "Amenity":
                        obj = Amenity(**objects[key])
                    if cls == "Review":
                        obj = Review(**objects[key])
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    self.__objects[key] = obj
