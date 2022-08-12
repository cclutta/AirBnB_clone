#!/usr/bin/python3
""" Base Model Module
Contains base model class.
"""

import uuid
import models
from datetime import datetime

class BaseModel:
    """ base of the classes in AirBnB clone
    
    Attributes:
        id: id for each instance
        created_at: date of instance creation
        updated_at: date of instance update
    """
    
    def __init__(self, *args, **kwargs):
        """ Initializes attributes of BaseModel
        
        Args:
            *args: args
            **kwargs: kwargs
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)
     def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with all the keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
