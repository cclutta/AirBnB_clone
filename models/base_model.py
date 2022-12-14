#!/usr/bin/python3
"""Module square
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class. """
    def __init__(self, *args, **kwargs):
        """Sets public instance attributes
        Args:
            args: args
            kwargs: kwargs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """ Prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns keys/values of __dict__ of the instance. """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
