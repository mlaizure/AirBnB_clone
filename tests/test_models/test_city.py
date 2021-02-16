#!/usr/bin/python3
""" Testing Base Model Module """

import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """ testing output from User class """

    def test_attrs(self):
        """ test attrs of City when created """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(City.name, "")
        self.assertEqual(city.state_id, "")
        self.assertEqual(City.state_id, "")
        self.assertIn("id", city.__dict__)
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())

    def test_set_attrs(self):
        """ test the attrs of City when set """
        city2 = City()
        city2.name = "Hawaii"
        self.assertEqual(city2.name, "Hawaii")
        city2.state_id = "<3"
        self.assertEqual(city2.state_id, "<3")
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")

    def test_inheritance(self):
        """ test the inheritance of City from BaseModel """
        city3 = City()
        self.assertIsInstance(city3, BaseModel)
        self.assertIsInstance(city3, City)
