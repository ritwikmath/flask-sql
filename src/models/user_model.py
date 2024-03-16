from src.models.base import Base
from src.helpers.db_session import session
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.models.base_model import BaseModel
from werkzeug.exceptions import BadRequest

class UserModel(BaseModel):
    def __init__(self):
        # self.__user_base = self.UserBase()
        pass

    @session
    def single(self, session, condition, serialization = False):
        user = session.query(self.UserBase).filter_by(**condition).first()
        if serialization:
            data = self.serialize(user)
            return data
        return user

    @session
    def index(self, session):
        users = session.query(self.UserBase).all()
        data = self.serialize(users)
        return data
    
    @session
    def create(self, session, data):
        user = self.UserBase(**data)
        session.add(user)
        session.flush()
        return user
    
    @session
    def update(self, session, condition, data):
        user = session.query(self.UserBase).filter_by(**condition).first()
        if not user:
            raise BadRequest('User not found')
        for k,v in data.items():
            setattr(user, k, v)
        session.commit()
    
    class UserBase(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True)
        name = Column(String(150), nullable=False)
        email = Column(String(150), nullable=False, unique=True)
        password = Column(String(150), nullable=False)
        registered_at = Column(DateTime, default=datetime.now, nullable=False)
        otp = Column(String(5), default=None)
