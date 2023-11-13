#!/bin/usr/python3
"""
tests for the base model class
"""


import unittest
from models.base_model import BaseModel


b1 = BaseModel()
dictionary = {'t Model',
b2 = BaseModel(**dictionary)


class TestBase(unittest.TestCase):
    """Inherited class to test base"""
    def test_base(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b2, BaseModel)

    def test_values(self):
        """Test if the base class values have been updated"""
        self.assertEqual(b2.id, "b6a6e15c-c67d-4312-9a75-9d084935e579")
        self.assertEqual(b2.my_number, 89)
        self.assertEqual(b2.name, 'My First Model',)
        str_create = b2.created_at.isoformat()
        self.assertEqual(str_create, '2017-09-28T21:05:54.119427')

    def test_create(self):
        """Tests if base class is created"""
        b3 = BaseModel(**dictionary)
        self.assertIsInstance(b3, BaseModel)
        self.assertEqual(b3.id, "b6a6e15c-c67d-4312-9a75-9d084935e579")
        self.assertEqual(b3.my_number, 89)
        self.assertEqual(b3.name, 'My First Model')
        str_create = b3.created_at.isoformat()
        self.assertEqual(str_create, '2017-09-28T21:05:54.119427')
