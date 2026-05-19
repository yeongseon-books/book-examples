# pyright: reportUnusedCallResult=false, reportAny=false, reportExplicitAny=false
from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def make_memory_engine(echo: bool = False) -> Engine:
    return create_engine("sqlite+pysqlite:///:memory:", echo=echo, future=True)


def temp_alembic_tree() -> Path:
    base = Path(tempfile.mkdtemp(prefix="alembic101_"))
    (base / "alembic" / "versions").mkdir(parents=True, exist_ok=True)
    (base / "alembic.ini").write_text(
        "[alembic]\nscript_location = alembic\n", encoding="utf-8"
    )
    return base


def ensure_version_table(engine: Engine, version: str = "base") -> None:
    with engine.begin() as conn:
        conn.execute(
            text(
                "CREATE TABLE IF NOT EXISTS alembic_version (version_num TEXT NOT NULL)"
            )
        )
        conn.execute(text("DELETE FROM alembic_version"))
        conn.execute(
            text("INSERT INTO alembic_version(version_num) VALUES (:v)"), {"v": version}
        )


def get_version(engine: Engine) -> str:
    with engine.connect() as conn:
        value = conn.execute(
            text("SELECT version_num FROM alembic_version")
        ).scalar_one()
    return str(value)


def rows_count(engine: Engine, table_name: str) -> int:
    with engine.connect() as conn:
        return int(
            conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar_one()
        )


def to_sqlite_url(path: Path) -> str:
    return f"sqlite:///{path}"


def as_bool(value: Any) -> bool:
    return str(value).lower() in {"1", "true", "yes", "on"}
