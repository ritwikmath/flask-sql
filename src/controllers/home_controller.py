from src.models.user_model import UserModel
import json
class HomeController:
    def __init__(self):
        self.__user_model = UserModel()

    def index(self):
        users = self.__user_model.index()
        return json.dumps({"data": users})