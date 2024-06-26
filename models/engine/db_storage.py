#!/usr/bin/python3
'''
DataBase Storage Module'''

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage:
    '''
    Database Engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiation
        '''
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_pwd = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_database = getenv('HBNB_MYSQL_DB')
        # Create engine
        # The string form of the URL is dialect[+driver]://user:password@host/dbname[?key=value..],
        self.__engine = create_engine(
            f'mysql+mysqldb://{MySQL_user}:{MySQL_pwd}@{MySQL_host}/{MySQL_database}', pool_pre_ping=True)
        # Get the env variable
        env_var = getenv('HBNB_ENV')
        # Drop all tables if env_var = 'test
        if env_var == 'test':
            Base.metadata.drop_all(bind=self.__engine)
    def all(self, cls=None):
            """Query on the curret database session all objects of the given class.

            If cls is None, queries all types of objects.

            Return:
                Dict of queried classes in the format <class name>.<obj id> = obj.
            """
            if cls is None:
                objs = self.__session.query(State).all()
                objs.extend(self.__session.query(City).all())
                objs.extend(self.__session.query(User).all())
                objs.extend(self.__session.query(Place).all())
                objs.extend(self.__session.query(Review).all())
                objs.extend(self.__session.query(Amenity).all())
            else:
                if type(cls) == str:
                    cls = eval(cls)
                objs = self.__session.query(cls)
            return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}


    def new(self, obj):
        '''add the object to the current database session 
        '''
        self.__session.add(obj)

    def save(self):
        ''' commit all changes of the current database session'''
        self.__session.commit()
    
    def delete(self, obj=None):
        '''delete from the current database session obj
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database &
        create the current database session
        '''
        # 1. Create tables
        Base.metadata.create_all(bind=self.__engine)
        # open session object to interact with data
        # 1.Session class is defined using sessionmaker()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        # 2.The session obj is then set up using its default constructor
        self.__session = Session()
        
        
    def close(self):
        """Close the working session."""
        self.__session.close()