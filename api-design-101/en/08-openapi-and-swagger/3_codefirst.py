# 3_codefirst.py
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int; name: str

app = FastAPI()
@app.get("/users/{uid}")
def user(uid: int) -> User: return User(id=uid, name="Y")
# /docs and /openapi.json are generated automatically
