#!/usr/bin/python3
""" Testing Amenity Module """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ testing output from User class """

    def test_attrs(self):
        """ test attrs of Amenity when created """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertEqual(Amenity.name, "")
        self.assertIn("id", amenity.__dict__)
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())

    def test_set_attrs(self):
        """ test the attrs of Amenity when set """
        amenity2 = Amenity()
        amenity2.name = "Beach Access"
        self.assertEqual(amenity2.name, "Beach Access")

    def test_inheritance(self):
        """ test the inheritance of Amenity from BaseModel """
        amenity3 = Amenity()
        self.assertIsInstance(amenity3, BaseModel)
        self.assertIsInstance(amenity3, Amenity)
