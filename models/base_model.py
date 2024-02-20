#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from uuid import uuid4
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models.
        Attributes:
            - id (String)
            - created_at (Datetime of creation)
            - updated_at (Datetime of laste update)
    """
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        '''Create dictionary from input arguments'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    '''Convert datetime string into obj'''
                    '''strptime is class method
                    so we call it on datetime'''
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    '''add items to dict'''
                    self.__dict__[key] = value


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        # Access the class name and add class key and value
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        # Convert to ISO format
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary['_sa_instance_state']:
            del dictionary['_sa_instance_state']
        return dictionary
    
    def delete(self):
        ''' delete the current instance from the storage
        '''
        models.storage.delete(self)
