"""Episode 06: Authentication and role-based authorization."""

import sys
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import bearer_user, make_auth_token


class LoginIn(BaseModel):
    username: str
    password: str


def build_app(secret: str = "dev-secret") -> FastAPI:
    app = FastAPI()

    @app.post("/login")
    def login(payload: LoginIn):
        if payload.password != "pw123":
            raise HTTPException(status_code=401, detail="invalid credentials")
        token = make_auth_token(payload.username, secret)
        return {"access_token": token}

    @app.get("/me")
    def me(user: dict[str, str] = Depends(bearer_user(secret))):
        return {"username": user["username"], "role": user["role"]}

    @app.delete("/admin/users/{user_id}")
    def delete_user(user_id: int, user: dict[str, str] = Depends(bearer_user(secret))):
        if user["role"] != "admin":
            raise HTTPException(status_code=403, detail="forbidden")
        return {"deleted": user_id}

    return app
