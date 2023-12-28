from flask import request
from src.models.user_model import UserModel
from src.validators.user_validator import UserValidator
from src.validators.auth_validator import AuthValidator
import jwt

class AuthController:
    def login(self):
        data = AuthValidator(**request.json)
        token = jwt.encode(data.model_dump(), "secret", algorithm="HS256")
        return {"token": token}

    def register(self):
        validated_data = UserValidator(**request.json)
        user = UserModel().create(validated_data.model_dump())
        data = {
            "id": user.id,
        }
        return {"message": "User registered successfully", "data": data}