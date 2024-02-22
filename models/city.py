#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    # one-to-many relationship with Place
    # if getenv("HBNB_TYPE_STORAGE") == "db":
    places = relationship("Place", back_populates="city", cascade="all, delete-orphan")

    # else:
    #     @property
    #     def places(self):
    #         """ Getter """
    #         from models.engine.file_storage import FileStorage
    #         storage = FileStorage()
    #         places_dict = storage.all(Place)
    #         return [place for place in places_dict.values() if place.city_id == self.id]


    #     @places.setter
    #     def places(self, value):
    #         """ setter """
    #         pass

