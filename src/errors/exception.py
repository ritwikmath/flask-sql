from flask import Response
import json

def handleException(e):
    resp = Response(json.dumps({"error":"Something went wring"}), 500)  
    return resp