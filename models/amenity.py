#!/usr/bin/python3
""" Amenity Module, based on BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel, has public class attribute
    name"""

    name = ""
