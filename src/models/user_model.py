from src.models import Base
from src.helpers.db_session import session
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class UserModel():
    def __init__(self):
        # self.__table = "users"
        # self.__user_base = self.UserBase()
        pass

    @session
    def single(self, session, condition):
        data = session.query(self.UserBase).filter_by(**condition).first()
        return data

    @session
    def index(self, session):
        data = session.query(self.UserBase).all()
        return data
    
    @session
    def create(self, session, data):
        user = self.UserBase(**data)
        session.add(user)
        session.flush()
        return user
    
    class UserBase(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True)
        name = Column(String(150), nullable=False)
        email = Column(String(150), nullable=False, unique=True)
        password = Column(String(150), nullable=False)
        registered_at = Column(DateTime, default=datetime.now, nullable=False)
