from pydantic import BaseModel, EmailStr, SecretStr

class UserValidator(BaseModel, validate_assignment=True):
    name: str
    email: EmailStr
    password: SecretStr