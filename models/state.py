#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.base_model import Base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
