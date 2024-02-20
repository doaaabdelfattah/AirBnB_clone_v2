from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    '''
    Database Engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiation
        '''
        # Retrieve MySQL connection details from environment variables
        MySQL_user = os.getenv('HBNB_MYSQL_USER')
        MySQL_pwd = os.getenv('HBNB_MYSQL_PWD')
        MySQL_host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        MySQL_database = os.getenv('HBNB_MYSQL_DB')
        # Create engine
        # The string form of the URL is dialect[+driver]://user:password@host/dbname[?key=value..],
        self.__engine = create_engine(
            f'mysql+mysqldb:///{MySQL_user}:{MySQL_pwd}@{MySQL_host}/{MySQL_database}', pool_pre_ping=True, echo=True)
        # Bind the engine to a metadata instance
        metadata = MetaData(bind=self.__engine)
        # Get the env variable
        env_var = os.getenv('HBNB_ENV')
        # Drop all tables if env_var = 'test
        if env_var == 'test':
            metadata.drop_all()

    def all(self, cls=None):
        '''query on the current database session '''
        classes = [User, State, City, Amenity, Review, Place]
        query = []
        dict = {}
        if cls is None:
            for _class in classes:
                query.extend(self.__session.query(_class).all())
        else:
            query = self.__session.query(cls).all()
        # the output will be like this:
        # query = [<User object at 0x7f7f59d31250>, <User object at 0x7f7f59d31590>]
        for obj in query:
            key = f"{obj.__class__.__name__}.{obj.id}"
            dict[key] = obj

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