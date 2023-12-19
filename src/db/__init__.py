import os
import mysql.connector

class Database:
    def __init__(self):
        self.__user = os.getenv("MYSQL_USER")
        self.__host = os.getenv("MYSQL_HOST")
        self.__pass = os.getenv("MYSQL_PASSWORD")
        self.__db = os.getenv("MYSQL_DB")

    def connect(self):
        cnx = mysql.connector.connect(user=self.__user, password=self.__pass,
                              host=self.__host,
                              database=self.__db)
        return cnx.cursor, cnx.close
