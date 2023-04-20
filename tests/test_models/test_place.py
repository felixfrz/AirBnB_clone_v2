#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for Place
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Tests for the model place"""

    def __init__(self, *args, **kwargs):
        """ Tests instantiation of place """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Tests attribute city_id """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Tests attribute user_id  """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ Tests attribute name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ Tests attribute description """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Tests attribute number_rooms """
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Tests attribute number_bathrooms """
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Tests attribute max_guest """
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test attribute price_by_night """
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test attribute latitude """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Tests attribute longitude """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)
