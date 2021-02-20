#!/usr/bin/python3
"""I hate typing comments"""
import json
import models
from models import BaseModel

class FileStorage:
    """neet im doing iwhat the FUCK have I donet again"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        F = (type(obj).__name__ + "." + obj.id)
        self.__objects[F] = obj

    def save(self):
        my_dict = {}
        for k in FileStorage.__objects:
            my_dict[k] = FileStorage.__objects[k].to_dict()
        with open(self.__file_path, mode="w+") as F:
            json.dump(my_dict, F)


    def reload(self):
        try:
            with open(self.__file_path, mode="r") as F:
                my_dict = json.load(F)
        
        except FileNotFoundError:
            pass
