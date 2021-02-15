#!/usr/bin/python3
""" City Module, based on BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel, public class attributes state_id
    and name"""

    state_id = ""
    name = ""
