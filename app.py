from flask import Flask
import os
from src.schema import Schema

app = Flask(__name__)

Schema().ma = app
print(Schema().ma)
from src.bootstrap import Bootstrap
Bootstrap(app)

if __name__ == "__main__":
    # Database().createTables()
    app.run(debug=os.getenv("ENV") == "DEV", host="0.0.0.0")