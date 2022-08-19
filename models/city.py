#!/usr/bin/python3
""" City Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Defines a city
    Attributes:
       state_id = state id
       name: name of the city
    """
    state_id = ""
    name = ""
