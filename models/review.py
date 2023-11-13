#!/usr/bin/python3
"""
review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
