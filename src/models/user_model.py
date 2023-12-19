from src.db import Database

class UserModel:
    def __init__(self):
        self.__cur, self.__close = Database().connect()
        self.__table = "users"
    
    def index(self):
        query = f"select user_id, username, email from {self.__table}"
        self.__cur.execute(query)
        return self.__cur.fetchall()