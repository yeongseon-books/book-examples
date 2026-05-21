# 2_routes.py
from fastapi import FastAPI

app = FastAPI()

USERS = [{"id": 1, "name": "Alice"}]

@app.get("/users")
def list_users():
    return USERS
