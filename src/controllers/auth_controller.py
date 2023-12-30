from flask import request
from src.models.user_model import UserModel
from src.validators.user_validator import UserValidator
from src.validators.login_validator import LoginValidator
from src.validators.password_reset_validator import PasswordResetValidator
import jwt
import bcrypt
from werkzeug.exceptions import Forbidden, BadRequest
from src.services.mail import MailService

class AuthController:
    def login(self):
        validated_data = LoginValidator(**request.json)
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
    
    def forget_password(self):
        otp = '12345'
        email = request.json.get('email')
        if not email:
            raise BadRequest('Invalid email')
        user = UserModel().single({"email": email})
        if not user:
            raise BadRequest("Email not registered")
        MailService(
            recipient=user.email,
            subject='Verification Code for Password Reset'
            ).format_mail(
                template_name='send_otp',
                varables=[('GENERATED_OTP', otp)]
            ).send_mail()
        UserModel().update({"email": email}, {'otp': otp})
        return {"message": "OTP sent to email"}

    def reset_password(self):
        validated_data = PasswordResetValidator(**request.json)
        post_data = validated_data.model_dump()
        user = UserModel().single({'email': post_data['email'], 'otp': post_data['otp']})
        if not user:
            raise BadRequest('Password reset failed')
        UserModel().update({"email": user.email}, {'otp': None, 'password': validated_data.password})
        return {"message": "Password reset successfully"}

        
        