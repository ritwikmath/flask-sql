from flask import Flask
import os
from src.bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.get("/")
def index():
    raise Exception("Nothing")

if __name__ == "__main__":
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")