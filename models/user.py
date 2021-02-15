#!/usr/bin/python3
""" User Module, base on BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ Creates a User:
    inherits from BaseModel
    adds email, password,
    first and last name. """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
