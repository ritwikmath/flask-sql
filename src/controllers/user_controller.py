from flask import request
from src.validators.user_validator import UserValidator
import json

class UserController:
    def create(self):
        data = UserValidator(**request.json)
        return json.loads(data.model_dump_json())