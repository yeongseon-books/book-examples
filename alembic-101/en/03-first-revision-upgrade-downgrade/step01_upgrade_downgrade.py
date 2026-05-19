from __future__ import annotations

from sqlalchemy import text

from common import make_memory_engine


def apply_upgrade_and_downgrade() -> dict[str, int]:
    engine = make_memory_engine()
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL)"))
        conn.execute(text("ALTER TABLE users ADD COLUMN tier TEXT NOT NULL DEFAULT 'free'"))
        cols_after_upgrade = [r[1] for r in conn.execute(text("PRAGMA table_info(users)"))]
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE users_new (id INTEGER PRIMARY KEY, email TEXT NOT NULL)"))
        conn.execute(text("INSERT INTO users_new(id, email) SELECT id, email FROM users"))
        conn.execute(text("DROP TABLE users"))
        conn.execute(text("ALTER TABLE users_new RENAME TO users"))
        cols_after_downgrade = [r[1] for r in conn.execute(text("PRAGMA table_info(users)"))]
    return {"upgrade_cols": len(cols_after_upgrade), "downgrade_cols": len(cols_after_downgrade)}


# English mirror
if __name__ == "__main__":
    print(apply_upgrade_and_downgrade())
