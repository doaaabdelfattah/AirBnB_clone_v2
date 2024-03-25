#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models.engine.file_storage import FileStorage
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    # Define relationship with City
    cities = relationship("City", backref="state", cascade="delete")

    # Define the getter method for cities
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter """
            cities_dict = models.storage.all(City)
            return [city for city in cities_dict.values() if city.state_id == self.id]
