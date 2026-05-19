import asyncio
import sqlite3

from common import setup_demo_db


async def run_with_thread_fallback() -> int:
    def blocking_count() -> int:
        conn = setup_demo_db()
        value = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        conn.close()
        return value

    return await asyncio.to_thread(blocking_count)


async def run_with_aiosqlite_if_available() -> int:
    try:
        import aiosqlite  # type: ignore
    except ImportError:
        return await run_with_thread_fallback()

    async with aiosqlite.connect(":memory:") as conn:
        await conn.executescript(
            """
            CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE);
            INSERT INTO users(name, email) VALUES ('A', 'a@example.com');
            INSERT INTO users(name, email) VALUES ('B', 'b@example.com');
            """
        )
        async with conn.execute("SELECT COUNT(*) FROM users") as cur:
            row = await cur.fetchone()
            return int(row[0])


def run_demo() -> dict[str, int]:
    count = asyncio.run(run_with_aiosqlite_if_available())
    return {"count": count}


if __name__ == "__main__":
    print(run_demo())
