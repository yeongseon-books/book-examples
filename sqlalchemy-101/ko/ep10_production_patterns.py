"""Sqlalchemy 101 - Episode 10: Production patterns."""

import time

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import scoped_session, sessionmaker


def run() -> dict[str, str]:
    """Run."""
    engine = create_engine(
        "sqlite:///:memory:",
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=False,
        future=True,
    )

    retries = 2
    last_error = ""
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("select 10"))
            break
        except OperationalError as exc:
            last_error = str(exc)
            time.sleep(0.01 * (attempt + 1))
    factory = sessionmaker(bind=engine, future=True)
    scoped = scoped_session(factory)
    with scoped() as session:
        value = session.execute(text("select 1")).scalar_one()
    scoped.remove()

    return {
        "pool": "configured",
        "retry": "ok" if not last_error else "recovered",
        "scoped": str(value),
        "migration": "Use Alembic for schema migrations.",
    }
