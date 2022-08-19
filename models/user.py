#!/usr/bin/python3
""" User Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a user

    Attributes:
        email: the email
        password: the password
        first_name: the first name
        last_name: the last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
