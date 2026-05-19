"""Python Dbapi 101 - Episode 6: Row factory."""

import dataclasses
import sqlite3

from common import setup_demo_db


@dataclasses.dataclass
class UserRecord:
    """User record."""

    id: int
    name: str
    email: str


def dataclass_factory(cursor, row):
    """Dataclass factory."""
    columns = [col[0] for col in cursor.description]
    data = dict(zip(columns, row, strict=False))
    return UserRecord(**data)


def run_demo() -> dict[str, object]:
    """Run demo."""
    conn = setup_demo_db()

    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT id, name, email FROM users WHERE id = 1").fetchone()
    row_name = row["name"]

    conn.row_factory = dataclass_factory
    record = conn.execute("SELECT id, name, email FROM users WHERE id = 2").fetchone()

    conn.close()
    return {
        "row_name": row_name,
        "record_type": type(record).__name__,
        "record_name": record.name,
    }


if __name__ == "__main__":
    print(run_demo())
