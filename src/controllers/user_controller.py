from flask import request
from src.validators.user_validator import UserValidator
import json
from src.models.user_model import UserModel

class UserController:
    def index(self):
        data = UserModel().index()
        return json.loads(json.dumps(data, default=str))

    def create(self):
        validated_data = UserValidator(**request.json)
        user = UserModel().create(validated_data.model_dump())
        print(user.id, user)
        data = {
            "id": user.id,
        }
        return {"message": "User added successfully", "data": data}