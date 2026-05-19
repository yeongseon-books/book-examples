from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from hmac import compare_digest
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


def make_sqlite_engine() -> Any:
    return create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


def init_db(engine: Any) -> None:
    Base.metadata.create_all(engine)


def make_auth_token(username: str, secret: str) -> str:
    digest = sha256(f"{username}:{secret}".encode()).hexdigest()
    return f"{username}.{digest}"


def verify_auth_token(token: str, secret: str) -> dict[str, str]:
    try:
        username, provided = token.split(".", 1)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="invalid token") from exc
    expected = sha256(f"{username}:{secret}".encode()).hexdigest()
    if not compare_digest(expected, provided):
        raise HTTPException(status_code=401, detail="invalid token")
    role = "admin" if username == "admin" else "user"
    return {"username": username, "role": role}


def bearer_user(secret: str):
    def _dep(authorization: str = Header(default="")) -> dict[str, str]:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="missing bearer token")
        token = authorization.removeprefix("Bearer ")
        return verify_auth_token(token, secret)

    return _dep


@dataclass
class InMemoryCache:
    values: dict[str, Any]

    def get(self, key: str) -> Any:
        return self.values.get(key)

    def set(self, key: str, value: Any) -> None:
        self.values[key] = value


@dataclass
class InMemoryQueue:
    jobs: list[dict[str, Any]]

    def enqueue(self, job_type: str, payload: dict[str, Any]) -> None:
        self.jobs.append({"type": job_type, "payload": payload})


def request_id_middleware(app: FastAPI) -> None:
    @app.middleware("http")
    async def add_request_id(request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", "rid-demo")
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response


def domain_error_handlers(app: FastAPI) -> None:
    class DomainError(Exception):
        def __init__(self, code: str, message: str):
            super().__init__(message)
            self.code = code
            self.message = message

    @app.exception_handler(DomainError)
    async def handle_domain_error(_: Request, exc: DomainError):
        return JSONResponse(
            status_code=400, content={"code": exc.code, "message": exc.message}
        )

    app.state.DomainError = DomainError


def list_user_names(session: Session) -> list[str]:
    return list(session.scalars(select(User.name)).all())
