#!/usr/bin/python3
""" File Storage Module """

import json

class FileStorage:
    """ Handles the serialization of class to JSON """
    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        self.__objects = {"home": "hi"}

    def all(self):
        """
            returns dict of self
        """
        return self.__objects

    def new(self, obj):
        """
            adds new obj to class dictionary
        """
        self.__objects["{}.{}".format(type(self).__name__, self.id)] = obj

    def save(self):
        """
            serializes objects to JSON
        """
        with open(self.__file_path, 'a+') as f:
            f.write("hello")
            for key, value in self.__objects:
                f.write(json.dumps(value))

    def reload(self):
        """
            deserializes the JSON file
        """
        with open(self.__file_path, 'a+') as f:
            self.__objects = json.load(f)
