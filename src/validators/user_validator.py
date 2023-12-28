from pydantic import BaseModel, EmailStr, SecretStr, field_validator
import bcrypt
import os
from src.models.user_model import UserModel

class UserValidator(BaseModel, validate_assignment=True):
    name: str
    email: EmailStr
    password: str

    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
    
    @field_validator('email')
    @classmethod
    def email_must_be_unqie(cls, v: str) -> str:
        user = UserModel().single({'email': v})
        if user:
            raise ValueError("must be unique")
        return v

    @field_validator('password')
    @classmethod
    def password_must_be_eight_to_fifteen_characters(cls, v: str) -> str:
        length = len(v)
        if length < 8 or length > 15:
            raise ValueError("must be between 8 to 15 characters")
        return bcrypt.hashpw(str(v).encode('utf-8'), f"{os.getenv('HASH_SECRET')}".encode('utf-8')).decode()