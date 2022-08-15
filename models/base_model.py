#!/usr/bin/python3
"""Module square
"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class. """
    def __init__(self):
        """Sets public instance attributes
        Args:
            id : string
            created_at: datetime
            updated_at: datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns keys/values of __dict__ of the instance. """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
