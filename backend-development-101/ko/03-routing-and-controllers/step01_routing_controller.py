"""Backend Development 101 - 3편: routing and controllers 예제."""

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


class UserIn(BaseModel):
    """User in."""

    name: str
    active: bool = True


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    router = APIRouter(prefix="/users", tags=["users"])

    @router.get("")
    def list_users(active: bool = True, limit: int = 10):
        """List users."""
        return {"active": active, "limit": limit}

    @router.get("/{user_id}")
    def get_user(user_id: int):
        """Get user."""
        return {"id": user_id}

    @router.post("")
    def create_user(payload: UserIn):
        """Create user."""
        return {"id": 1, "name": payload.name, "active": payload.active}

    app.include_router(router)
    return app
