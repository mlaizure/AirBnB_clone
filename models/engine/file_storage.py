#!/usr/bin/python3
""" File Storage Module """
import json
from os import path


class FileStorage:
    """ Handles the serialization of class to JSON """
    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
            returns dict of self
        """
        return self.__objects

    def new(self, obj):
        """
            adds new obj to class dictionary
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
            serializes objects to JSON
        """
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps({key: value.to_dict() for key, value
                                in self.__objects.items()}))

    def reload(self):
        """
            deserializes the JSON file
        """
        from ..base_model import BaseModel
        from models.user import User
        cl_names = {"BaseModel": BaseModel, "User": User}
        if not path.exists(self.__file_path):
            pass
        elif path.getsize(self.__file_path) == 0:
            pass
        else:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                cl_nm = cl_names.get(key.split('.')[0])
                self.__objects[key] = cl_nm(**value)
