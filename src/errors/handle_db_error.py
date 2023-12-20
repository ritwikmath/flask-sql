from flask import jsonify
import traceback
import os
import sys

def handleDbError(e):
    data = {"error":"Service unavailable"}
    if os.getenv("ENV") == "DEV":
        data.update({
            "traceback": traceback.format_exc()
        })
    return jsonify(data), 502