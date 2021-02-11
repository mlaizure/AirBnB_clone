#!/usr/bin/python3
"""Module containing base class"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes attributes from base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key is "__class__":
                    continue
                elif key is "created_at" or key is "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """returns a human readable string for pretty printing"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates public instance attribute updated_at with current
        datetime"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict__
        of the instance"""
        my_dict = self.__dict__
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = str(self.created_at.isoformat())
        my_dict['updated_at'] = str(self.updated_at.isoformat())
        return my_dict
