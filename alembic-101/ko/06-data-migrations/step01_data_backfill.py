from __future__ import annotations

from sqlalchemy import text

from common import make_memory_engine


def backfill_tier(batch_size: int = 2) -> int:
    engine = make_memory_engine()
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, tier TEXT)"))
        for i in range(1, 6):
            conn.execute(text("INSERT INTO users(id, name, tier) VALUES (:i, :n, NULL)"), {"i": i, "n": f"u{i}"})
        changed = 0
        while True:
            ids = conn.execute(text("SELECT id FROM users WHERE tier IS NULL LIMIT :n"), {"n": batch_size}).fetchall()
            if not ids:
                break
            for (user_id,) in ids:
                conn.execute(text("UPDATE users SET tier='free' WHERE id=:i AND tier IS NULL"), {"i": user_id})
                changed += 1
    return changed


if __name__ == "__main__":
    print(backfill_tier())
