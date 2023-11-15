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
            for key in kwargs:
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
                if key == "email":
                    self.email = kwargs[key]
                if key == "password":
                    self.password = kwargs[key]
                if key == "first_name":
                    self.first_name = kwargs[key]
                if key == "last_name":
                    self.last_name = kwargs[key]
                if key == "state_id":
                    self.state_id = kwargs[key]
                if key == "city_id":
                    self.city_id = kwargs[key]
                if key == "user_id":
                    self.user_id = kwargs[key]
                if key == "description":
                    self.description = kwargs[key]
                if key == "number_rooms":
                    self.number_rooms = kwargs[key]
                if key == "number_bathrooms":
                    self.number_bathrooms = kwargs[key]
                if key == "price_by_night":
                    self.price_by_night = kwargs[key]
                if key == "max_guest":
                    self.max_guest = kwargs[key]
                if key == "latitude":
                    self.latitude = kwargs[key]
                if key == "longtitude":
                    self.longtitude = kwargs[key]
                if key == "amenity_ids":
                    self.amenity_ids = kwargs[key]
                if key == "place_id":
                    self.place_id = kwargs[key]
                if key == "text":
                    self.text = kwargs[key]
                # setattr(self.__class__, key, kwargs[key])
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
