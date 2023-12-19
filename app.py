from flask import Flask
import os
from src.bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

if __name__ == "__main__":
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")