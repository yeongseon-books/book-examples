"""Episode 03: Router and controller separation."""

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    active: bool = True


def build_app() -> FastAPI:
    app = FastAPI()
    router = APIRouter(prefix="/users", tags=["users"])

    @router.get("")
    def list_users(active: bool = True, limit: int = 10):
        return {"active": active, "limit": limit}

    @router.get("/{user_id}")
    def get_user(user_id: int):
        return {"id": user_id}

    @router.post("")
    def create_user(payload: UserIn):
        return {"id": 1, "name": payload.name, "active": payload.active}

    app.include_router(router)
    return app
