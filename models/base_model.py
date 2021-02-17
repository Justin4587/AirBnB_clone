#!/usr/bin/python3
"""Class base"""
import uuid
from datetime import datetime


class BaseModel:
    """still base modeling is that a word"""

    def __init__(self, *args, **kwargs):
        """If it is its not spelt right ??? spelt"""

        if kwargs != None and len(kwargs) != 0:
            for k in kwargs:
                if k == "id":
                    self.id = kwargs[k]
                elif k == "created_at":
                    self.created_at = datetime.strptime(kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if k == "updated_at":
                        self.updated_at = datetime.strptime(kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            
    def to_dict(self):
        """ something something darkside"""
        my_dict = dict(self.__dict__).copy()
        my_dict.update(self.__dict__)

        for k in my_dict:
            if k == "id":
                my_dict[k] = self.id
            elif k == "created_at":
                my_dict[k] = self.created_at.isoformat()
            elif k == "updated_at":
                my_dict[k] = self.updated_at.isoformat()
            
        my_dict["__class__"] = type(self)

        return my_dict

    
    def __str__(self):
        """ str rep of object """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """updates"""
        self.updated_at = datetime.now()
