#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel
"""


from models.base_model import BaseModel
from models.__init__ import storage


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
