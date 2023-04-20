#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for City
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Tests for the model city"""

    def __init__(self, *args, **kwargs):
        """ Tests instantiation of city """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Tests attribute state_id """
        new = self.value()
        self.assertNotEqual(type(new.state_id), str)

    def test_name(self):
        """ Tests attribute name """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
