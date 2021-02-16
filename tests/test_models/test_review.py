#!/usr/bin/python3
""" Testing Review Module """

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """ testing output from Review class """

    def test_attrs(self):
        """ test attrs of Review when created """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertEqual(Review.text, "")
        self.assertIn("id", review.__dict__)
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())

    def test_set_attrs(self):
        """ test the attrs of Review when set """
        review2 = Review()
        review2.place_id = "5678"
        review2.user_id = "Jack The House Man"
        review2.text = "First warm, then cold, nice guy Jack is."
        self.assertEqual(review2.place_id, "5678")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(review2.user_id, "Jack The House Man")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(review2.text, "First warm, then cold,"
                                       " nice guy Jack is.")
        self.assertEqual(Review.text, "")

    def test_inheritance(self):
        """ test the inheritance of Review from BaseModel """
        review3 = Review()
        self.assertIsInstance(review3, BaseModel)
        self.assertIsInstance(review3, Review)
