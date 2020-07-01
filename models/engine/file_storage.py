#!/usr/bin/python3



import json
import models
from models.base_model import BaseModel


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        aux = {}
        for key, value in self.__objects.items():
            aux[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(aux, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as filesave:
                # dic = json.load(f)
                for key, value in json.load(filesave).items():
                    aux = eval(value['__class__'])(**value)
                    self.__objects[key] = aux
        except Exception:
            pass
