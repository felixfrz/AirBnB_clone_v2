#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for State
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Tests for the model State"""

    def __init__(self, *args, **kwargs):
        """ Test instantiation of state"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test attribute """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
