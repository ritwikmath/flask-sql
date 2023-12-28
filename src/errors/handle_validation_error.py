from flask import jsonify
import traceback
import os

def handleValidationError(e):
    err_messages = [f"{error.get('loc')[0]} {error.get('msg')}".capitalize().replace(" value error,", "") for error in e.errors()]
    data = {"error": err_messages}
    return jsonify(data), 502