#!/usr/bin/python3
""" Testing State Module """

import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """ testing output from User class """

    def test_attrs(self):
        """ test attrs of State when created """
        state = State()
        self.assertEqual(state.name, "")
        self.assertEqual(State.name, "")
        self.assertIn("id", state.__dict__)
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())

    def test_set_attrs(self):
        """ test the attrs of State when set """
        state2 = State()
        state2.name = "Hawaii"
        self.assertEqual(state2.name, "Hawaii")

    def test_inheritance(self):
        """ test the inheritance of State from BaseModel """
        state3 = State()
        self.assertIsInstance(state3, BaseModel)
        self.assertIsInstance(state3, State)
