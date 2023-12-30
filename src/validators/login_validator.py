from pydantic import BaseModel, EmailStr, field_validator
from src.models.user_model import UserModel

class LoginValidator(BaseModel, validate_assignment=True):
    email: EmailStr
    password: str
    
    @field_validator('email')
    @classmethod
    def email_must_be_unqie(cls, v: str) -> str:
        user = UserModel().single({'email': v})
        if not user:
            raise ValueError("not registered")
        return v