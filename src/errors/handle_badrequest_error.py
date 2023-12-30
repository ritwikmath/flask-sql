from flask import jsonify

def handleBadRequestError(e):
    data = {"error": e.__str__().split(": ")[1]}
    return jsonify(data), 400