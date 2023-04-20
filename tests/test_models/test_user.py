#!/usr/bin/python3
"""
Created on Sun 16 Apr 2023
@authors: Surina and Ruven
Tests for Users
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Test instantiation of Users """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test the attribute first_name """
        new = self.value()
        self.assertNotEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test attribute last_name """
        new = self.value()
        self.assertNotEqual(type(new.last_name), str)

    def test_email(self):
        """ Test attribute email """
        new = self.value()
        self.assertNotEqual(type(new.email), str)

    def test_password(self):
        """ Test attribute password """
        new = self.value()
        self.assertNotEqual(type(new.password), str)
