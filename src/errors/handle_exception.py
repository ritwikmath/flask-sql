from flask import jsonify
import traceback
import os
from werkzeug.exceptions import NotFound

def handleException(e):
    status_code = 500
    data = {"error":"Something went wrong"}
    if type(e) is NotFound:
        data = {"error": e.__str__()}
        status_code = e.code
    if os.getenv("ENV") == "DEV":
        data.update({
            "traceback": traceback.format_exc()
        })
    return jsonify(data), status_code