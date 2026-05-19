"""Sqlalchemy 101 - Episode 3: Core crud."""

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    delete,
    insert,
    select,
    update,
)


def run() -> dict[str, str]:
    """Run."""
    metadata = MetaData()
    users = Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50), nullable=False),
    )
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)

    with engine.begin() as conn:
        conn.execute(insert(users).values(id=1, name="alice"))
        before = conn.execute(select(users.c.name).where(users.c.id == 1)).scalar_one()
        conn.execute(update(users).where(users.c.id == 1).values(name="alice-updated"))
        after = conn.execute(select(users.c.name).where(users.c.id == 1)).scalar_one()
        conn.execute(delete(users).where(users.c.id == 1))
        remaining = conn.execute(select(users.c.id)).all()

    return {"before": before, "after": after, "count": str(len(remaining))}
