#!/usr/bin/python3
""" File Storage Module """
import json
from os import path


class FileStorage:
    """ Handles the serialization of class to JSON """
    __file_path = "file.json"
    __objects = {}

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
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        cl_names = {"BaseModel": BaseModel, "User": User, "State": State,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review}
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
