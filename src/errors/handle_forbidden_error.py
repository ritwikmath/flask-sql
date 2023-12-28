from flask import jsonify

def handleForbiddenError(e):
    data = {"error": e.__str__().split(": ")[1]}
    return jsonify(data), 403