#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for Amenity
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests model amenity """

    def __init__(self, *args, **kwargs):
        """ Tests instantiation of model Amenity """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Tests attribute name """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
