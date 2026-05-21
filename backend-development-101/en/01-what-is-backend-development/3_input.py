# 3_input.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    name: str

@app.post("/users")
def create_user(payload: UserIn):
    return {"id": 99, "name": payload.name}
