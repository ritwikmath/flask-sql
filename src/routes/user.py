from flask import Blueprint
from src.controllers.user_controller import UserController

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.post("")
def create():
    return UserController().create()