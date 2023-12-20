from src.models import Model
from src.db import Database

class UserModel(Model):
    def __init__(self):
        self.__cur, self.__conn_close = Database().connect()
        self.__table = "users"
    
    def index(self):
        query = f"select user_id, username, email from {self.__table}"
        self.__cur.execute(query)
        data = self.__cur.fetchall()
        self.__cur.close()
        self.__conn_close()
        return data