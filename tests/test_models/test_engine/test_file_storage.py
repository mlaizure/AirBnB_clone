#!/usr/bin/python3
""" Testing File Storage Module """

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ testing output from FileStorage class """

    @classmethod
    def setUpClass(cls):
        """sets up class instances for tests"""
        cls.BM = BaseModel()
        cls.BM1 = BaseModel()
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """deletes instances after tests"""
        del cls.BM
        del cls.BM1
        del cls.storage

    def test_all(self):
        """test all method of file storage"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        key = "{}.{}".format(type(self.BM).__name__, self.BM.id)
        self.assertIn(key, objects)
        self.assertEqual(self.BM, objects.get(key))
        key1 = "{}.{}".format(type(self.BM1).__name__, self.BM1.id)
        self.assertIn(key1, objects)
        self.assertEqual(self.BM1, objects.get(key1))

    def test_new(self):
        """test new method of file storage"""
        attr_dict = {"attribute": "value"}
        new_obj = BaseModel(**attr_dict)
        objects = self.storage.all()
        key_new = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertNotIn(key_new, objects)
        self.storage.new(new_obj)
        self.assertIn(key_new, objects)
        key = "{}.{}".format(type(self.BM).__name__, self.BM.id)
        self.assertIn(key_new, objects)
        self.assertEqual(self.BM, objects.get(key))

    def test_save(self):
        """test save method of file storage"""
        objects = self.storage.all()
        self.storage.save()
        with open("file.json", 'r') as f:
            from_file = f.read()
        self.assertEqual(from_file, json.dumps({key: value.to_dict()
                                                for key, value in
                                                objects.items()}))

    def test_reload(self):
        """test reload method of file storage"""
        before = self.storage.all()
        self.storage.reload()
        after = self.storage.all()
        self.assertDictEqual(before, after)
