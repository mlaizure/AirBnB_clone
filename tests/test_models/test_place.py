#!/usr/bin/python3
""" Testing Place Module """

import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ testing output from User class """

    def test_attrs(self):
        """ test attrs of Place when created """
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(Place.amenity_ids, [])
        self.assertIn("id", place.__dict__)
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())

    def test_set_attrs(self):
        """ test the attrs of Place when set """
        place2 = Place()
        place2.name = "Le House"
        place2.city_id = "1234"
        place2.user_id = "Jack The House Man"
        place2.description = "terrible"
        place2.number_rooms = 1
        place2.number_bathrooms = 8
        place2.max_guest = 3
        place2.price_by_night = 7392
        place2.latitude = 5.5
        place2.longitude = 5.5
        place2.amenity_ids = ["lame", "upscale",
                              "forward thinking",
                              "distant", "aloof"]
        self.assertEqual(place2.name, "Le House")
        self.assertEqual(Place.name, "")
        self.assertEqual(place2.city_id, "1234")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(place2.user_id, "Jack The House Man")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(place2.description, "terrible")
        self.assertEqual(Place.description, "")
        self.assertEqual(place2.number_rooms, 1)
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(place2.number_bathrooms, 8)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(place2.max_guest, 3)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(place2.price_by_night, 7392)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(place2.latitude, 5.5)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(place2.longitude, 5.5)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(place2.amenity_ids, ["lame", "upscale",
                                              "forward thinking",
                                              "distant", "aloof"])
        self.assertEqual(Place.amenity_ids, [])

    def test_inheritance(self):
        """ test the inheritance of Place from BaseModel """
        place3 = Place()
        self.assertIsInstance(place3, BaseModel)
        self.assertIsInstance(place3, Place)
