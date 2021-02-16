#!/usr/bin/python3
""" Testing Base Model Module """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ testing output from BaseModel class """

    def test_init(self):
        """ testing init of attributes """
        BM = BaseModel()
        BM.id = 12
        BM_dict = {"created_at": "2021-02-16T15:53:02.772060",
                   "updated_at": "2021-02-16T15:53:02.772085",
                   "id": "d30aaea6-89e5-4381-b772-046fb7b452c7",
                   "first_name": "Reginald"}
        BM_kwargs = BaseModel(**BM_dict)
        self.assertEqual(BM.id, 12)
        self.assertIsInstance(BM, BaseModel)
        self.assertIsNotNone(BM.created_at)
        self.assertIsNotNone(BM.updated_at)
        self.assertIn("created_at", BM.__dict__)
        self.assertIn("updated_at", BM.__dict__)
        self.assertIn("id", BM.__dict__)
        self.assertIsInstance(BM.created_at, datetime)
        self.assertIsInstance(BM.updated_at, datetime)
        self.assertEqual(BM_kwargs.id, "d30aaea6-89e5-4381-b772-046fb7b452c7")
        self.assertIsInstance(BM_kwargs, BaseModel)
        self.assertIsNotNone(BM.created_at)
        self.assertIsNotNone(BM.updated_at)
        self.assertIn("created_at", BM_kwargs.__dict__)
        self.assertIn("updated_at", BM_kwargs.__dict__)
        self.assertIn("id", BM_kwargs.__dict__)
        self.assertIsInstance(BM_kwargs.created_at, datetime)
        self.assertIsInstance(BM_kwargs.updated_at, datetime)

    def test_str(self):
        """ testing the str method """
        BL = BaseModel()
        BL_str = str(BL)
        BL_format = "[BaseModel] ({}) {}".format(BL.id, BL.__dict__)
        self.assertEqual(BL_str, BL_format)

    def test_dict(self):
        """ testing the to dict method """
        BK = BaseModel()
        dict_test = BK.to_dict()
        self.assertIn('__class__', dict_test)
        self.assertIn("updated_at", dict_test)
        self.assertIn("created_at", dict_test)
        self.assertIn("id", dict_test)
        self.assertEqual(dict_test.get("updated_at"),
                         str(BK.updated_at.isoformat()))
        self.assertEqual(dict_test.get("created_at"),
                         str(BK.created_at.isoformat()))

    def test_save(self):
        """ tests the save method of BaseModel """
        BH = BaseModel()
        time = BH.updated_at
        BH.save()
        self.assertGreater(BH.updated_at, time)
