#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Float, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

# Define Table
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []
     
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Getter """
            storage = FileStorage()
            reviews_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
        
        @property
        def amenities(self):
            """ Get/set Amenities """
            amenity_list=[]
            amenity_dict = models.storage.all(Amenity)
            for amenity in list(amenity_dict.values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
        
        @amenities.setter
        def amenities(self, value):
            """Setter attribute that handles appending Amenity.id to amenity_ids list
            """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
