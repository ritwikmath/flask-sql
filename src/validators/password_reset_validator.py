from pydantic import BaseModel, EmailStr, field_validator
from src.models.user_model import UserModel
import bcrypt
import os

class PasswordResetValidator(BaseModel, validate_assignment=True):
    email: EmailStr
    password: str
    otp: str
    
    @field_validator('email')
    @classmethod
    def email_must_be_unqie(cls, v: str) -> str:
        user = UserModel().single({'email': v})
        if not user:
            raise ValueError("not registered")
        return v
    
    @field_validator('otp')
    @classmethod
    def otp_length(cls, v: str) -> str:
        if len(v) != 5:
            raise ValueError("format ivalid")
        return v

    @field_validator('password')
    @classmethod
    def password_must_be_eight_to_fifteen_characters(cls, v: str) -> str:
        length = len(v)
        if length < 8 or length > 15:
            raise ValueError("must be between 8 to 15 characters")
        return bcrypt.hashpw(str(v).encode('utf-8'), f"{os.getenv('HASH_SECRET')}".encode('utf-8')).decode()
