from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def index():
    return "Working"

if __name__ == "__main__":
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")