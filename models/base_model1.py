#!/usr/bin/python3
"""Base model 1
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Class BaseModel
    """

    def __init__(self, id=None):
        """Method constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a readable string
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """The method updates the instance attribute updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of instance
        """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__l
        return (new_dict)

class BaseModel1:
    """class BaseModel1
    """

    def __init__(self, *args, **kwargs):
        """Method constructor
        """
        self.args = args
        self.kwargs = 



