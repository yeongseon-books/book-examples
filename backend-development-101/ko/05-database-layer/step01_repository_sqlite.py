"""에피소드 05: SQLAlchemy repository와 트랜잭션 예제입니다."""

import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import User, init_db, list_user_names, make_sqlite_engine


class UserIn(BaseModel):
    name: str


def build_app() -> FastAPI:
    app = FastAPI()
    engine = make_sqlite_engine()
    init_db(engine)

    @app.post("/users")
    def create_user(payload: UserIn):
        with Session(engine) as session, session.begin():
            user = User(name=payload.name)
            session.add(user)
            session.flush()
            return {"id": user.id, "name": user.name}

    @app.get("/users")
    def get_users():
        with Session(engine) as session:
            return {"users": list_user_names(session)}

    return app
