from flask import Blueprint
from src.controllers.home_controller import HomeController

home_bp = Blueprint("home", __name__, url_prefix="/")

@home_bp.get("")
def index():
    return HomeController().index()