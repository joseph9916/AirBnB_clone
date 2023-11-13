#!/usr/bin/python#!/usr/bin/python33
"""
a command interpreter to manage AirBnB objects
"""


import uuid
from datetime import datetime
import copy


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """initialise new base model"""
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs[key]
                if key == "name":
                    self.name = kwargs[key]
                if key == "updated_at":
                    self.updated_at = (datetime.strptime
                                       (kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                if key == "created_at":
                    self.created_at = (datetime.strptime
                                       (kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                if key == "my_number":
                    self.my_number = kwargs[key]
        else:
            from models.__init__ import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Unofficial representation of class"""
        string = ("[{}] ({}) {}".format
                  (self.__class__.__name__, self.id, self.__dict__))
        return string

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance:
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = "{}".format(self.__class__.__name__)
        created_date = copy.deepcopy(self.created_at)
        if not isinstance(self.created_at, str):
            dictionary["created_at"] = created_date.isoformat()
        else:
            self.created_at = (datetime.strptime
                               (self.created_at, "%Y-%m-%dT%H:%M:%S.%f"))
        updated_date = copy.deepcopy(self.updated_at)
        if not isinstance(self.updated_at, str):
            dictionary["updated_at"] = updated_date.isoformat()
        else:
            self.updated_at = (datetime.strptime
                               (self.updated_at, "%Y-%m-%dT%H:%M:%S.%f"))
        return dictionary
