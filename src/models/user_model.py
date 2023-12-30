from src.models import Base
from src.helpers.db_session import session
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.schema.user_schema import UserSchema
class UserModel():
    def __init__(self):
        self.__user_schema = UserSchema(many=True)
        # self.__user_base = self.UserBase()
        pass

    @session
    def single(self, session, condition):
        user = session.query(self.UserBase).filter_by(**condition).first()
        data = self.__user_schema.dump(user)
        return data

    @session
    def index(self, session):
        users = session.query(self.UserBase).all()
        data = self.__user_schema.dump(users)
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
