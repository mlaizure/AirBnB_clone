#!/usr/bin/python3
""" init for file storage """

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()