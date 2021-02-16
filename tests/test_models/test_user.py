#!/usr/bin/python3
""" Testing User Module """

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """ testing output from User class """

    def test_attrs(self):
        """ test attrs of User when created """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")
        self.assertIn("id", user.__dict__)
        self.assertIn("created_at", user.__dict__)
        self.assertIn("updated_at", user.__dict__)
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_set_attrs(self):
        """ test the attrs of User when set """
        user1 = User()
        user1.email = "lol@gmail.com"
        self.assertEqual(user1.email, "lol@gmail.com")
        user1.password = "ProperElocutionIsImportant"
        self.assertEqual(user1.password, "ProperElocutionIsImportant")
        user1.first_name = "Lady Linda"
        self.assertEqual(user1.first_name, "Lady Linda")
        user1.last_name = "De Sol"
        self.assertEqual(user1.last_name, "De Sol")

    def test_inheritance(self):
        """ test the inheritance of User from BaseModel """
        user2 = User()
        self.assertIsInstance(user2, BaseModel)
        self.assertIsInstance(user2, User)

    def test_dict(self):
        """ tests the inherited to_dict method """
        user3 = User()
        dict_test = user3.to_dict()
        self.assertIn("__class__", dict_test)
        self.assertIn("created_at", dict_test)
        self.assertIn("updated_at", dict_test)
