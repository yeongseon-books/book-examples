"""Generated from book-content article."""

from sqlalchemy import String, column, table


def upgrade() -> None:
    users = table("users", column("tier", String))
    op.execute(
        users.update()
        .where(users.c.tier.is_(None))
        .values(tier="free")
    )
