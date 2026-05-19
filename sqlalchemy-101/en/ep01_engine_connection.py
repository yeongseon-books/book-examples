from sqlalchemy import text

from common import sync_engine


def run() -> int:
    engine = sync_engine()
    with engine.connect() as conn:
        value = conn.execute(text("select 1")).scalar_one()
    return int(value)
