"""Episode 05: SQLAlchemy repository and transaction flow."""

import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import User, init_db, list_user_names, make_sqlite_engine


class UserIn(BaseModel):
    """User in."""

    name: str


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    engine = make_sqlite_engine()
    init_db(engine)

    @app.post("/users")
    def create_user(payload: UserIn):
        """Create user."""
        with Session(engine) as session, session.begin():
            user = User(name=payload.name)
            session.add(user)
            session.flush()
            return {"id": user.id, "name": user.name}

    @app.get("/users")
    def get_users():
        """Get users."""
        with Session(engine) as session:
            return {"users": list_user_names(session)}

    return app
