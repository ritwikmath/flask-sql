from flask import Blueprint
from src.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.post("/signin")
def signin():
    return AuthController().login()

@auth_bp.post("/signup")
def signup():
    return AuthController().register()
