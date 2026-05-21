# 2_validation.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.post("/users")
def create():
    body = request.get_json() or {}
    errs = []
    if "name" not in body: errs.append({"field": "name", "code": "required"})
    if "email" not in body: errs.append({"field": "email", "code": "required"})
    if errs:
        return jsonify(title="Validation failed", status=422,
                       code="validation_error", errors=errs), 422
    return jsonify(ok=True), 201
