#!/usr/bin/python3
"""I hate typing comments"""
import json
from models.base_model import BaseModel

class FileStorage:
    """neet im doing it again"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FileName = (type(obj).__name__ + "." + obj.id)
        self.__objects[FileName] = obj
