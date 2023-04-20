#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for State
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Tests for model review"""

    def __init__(self, *args, **kwargs):
        """ Tests instantiation of review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Tests attribute place_id """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Tests attribute user_id """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ Tests attribute text """
        new = self.value()
        self.assertNotEqual(type(new.text), str)
