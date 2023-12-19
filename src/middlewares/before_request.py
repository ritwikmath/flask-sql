from flask import request, jsonify

def beforeRequest():
    if request.headers.get("Authorization") == "hello123" and request.method != "OPTIONS":
        return jsonify({"error": "Not authenticated"}), 401