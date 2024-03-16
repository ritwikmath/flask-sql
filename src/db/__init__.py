import os
import mysql.connector
from sqlalchemy import create_engine
from src.models.base import Base
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        self.__user = os.getenv("MYSQL_USER")
        self.__host = os.getenv("MYSQL_HOST")
        self.__pass = os.getenv("MYSQL_PASSWORD")
        self.__db = os.getenv("MYSQL_DB")
        self.__port  = (os.getenv("MYSQL_PORT"))

    def __createEngine(self):
        return create_engine(f"mysql+mysqlconnector://{self.__user}:{self.__pass}@{self.__host}:{self.__port}/{self.__db}", echo='debug')
    
    def createTables(self):
        engine = self.__createEngine()
        Base.metadata.create_all(engine)

    def __enter__(self):
        engine = self.__createEngine()
        Session = sessionmaker(bind = engine)
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.expunge_all()
        self.session.commit()
        self.session.close()
