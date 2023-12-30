from flask import Flask, g
from flask_mail import Mail
import os
from src.schema import Schema
# from src.db import Database

app = Flask(__name__)

Schema().ma = app
mail = Mail(app)
from src.bootstrap import Bootstrap
Bootstrap(app)

if __name__ == "__main__":
    # Database().createTables()
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")
