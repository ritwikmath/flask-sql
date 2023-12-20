from src.models.user_model import UserModel
import json
from src.validators.user_validator import UserValidator

class HomeController:
    def __init__(self):
        self.__user_model = UserModel()

    def index(self):
        users = self.__user_model.index()
        return json.dumps({"data": users})