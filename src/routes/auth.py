from flask import Blueprint
from src.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.post("/signin")
def signin():
    return AuthController().login()

@auth_bp.post("/signup")
def signup():
    return AuthController().register()

@auth_bp.post("/forget-password")
def forget_password():
    return AuthController().forget_password()

@auth_bp.post("/reset-password")
def reset_password():
    return AuthController().reset_password()
