#!/usr/bin/python3
""" Review Module, based on BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inhertis from BaseModel, has public class attributes
    place_id, user_id, and text"""

    place_id = ""
    user_id = ""
    text = ""
