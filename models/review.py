#!/usr/bin/python3
""" Review Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines a review
    Attributes:
       place_id: the place being reviewed
       user_id: id of the user
       text: the review
    """
    place_id = ""
    user_id = ""
    text = ""
