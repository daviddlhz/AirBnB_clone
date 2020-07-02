#!/usr/bin/python3
"""
FileStorage Class - serializes and deserializes JSON file to instances
"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with class name and id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serialization """
        aux = {}
        for key, value in self.__objects.items():
            aux[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(aux, f)

    def reload(self):
        """ deserialization """

        cl = {'BaseModel': BaseModel,
              'User': User, 'Place': Place,
              'State': State, 'City': City,
              'Amenity': Amenity, 'Review': Review}

        try:
            with open(self.__file_path, 'r') as filesave:
                for key, value in json.load(filesave).items():
                    if value['__class__'] in cl:
                        aux = eval(value['__class__'])(**value)
                        self.__objects[key] = aux

        except Exception:
            pass
