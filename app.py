from flask import Flask
import os
from src.bootstrap import Bootstrap
from src.db import Database

app = Flask(__name__)

Bootstrap(app)

if __name__ == "__main__":
    # Database().createTables()
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")