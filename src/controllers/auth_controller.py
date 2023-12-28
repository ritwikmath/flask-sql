from flask import request
from src.models.user_model import UserModel
from src.validators.user_validator import UserValidator
from src.validators.auth_validator import AuthValidator
import jwt
import bcrypt
from werkzeug.exceptions import Forbidden

class AuthController:
    def login(self):
        validated_data = AuthValidator(**request.json)
        data = UserModel().single({"email": validated_data.model_dump()['email']})
        if not bcrypt.checkpw(validated_data.password.encode('utf-8'), data.password.encode('utf-8')):
            raise Forbidden('Password did not match')
        tokenize_data = {
            "name": data.name,
            "email": data.email,
            "registered_at": data.registered_at.strftime("%m/%d/%Y, %H:%M:%S")
        }
        token = jwt.encode(tokenize_data, "secret", algorithm="HS256")
        return {"token": token}

    def register(self):
        validated_data = UserValidator(**request.json)
        user = UserModel().create(validated_data.model_dump())
        data = {
            "id": user.id,
        }
        return {"message": "User registered successfully", "data": data}