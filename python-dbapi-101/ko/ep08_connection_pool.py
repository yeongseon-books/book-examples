import queue
from contextlib import contextmanager

from common import create_connection, initialize_schema


class SqliteConnectionPool:
    def __init__(self, size: int = 2):
        self._queue: queue.Queue = queue.Queue(maxsize=size)
        for _ in range(size):
            conn = create_connection(":memory:")
            initialize_schema(conn)
            self._queue.put(conn)

    @contextmanager
    def acquire(self):
        conn = self._queue.get(timeout=1)
        try:
            yield conn
        finally:
            self._queue.put(conn)

    def closeall(self) -> None:
        while not self._queue.empty():
            self._queue.get_nowait().close()


def run_demo() -> dict[str, int]:
    pool = SqliteConnectionPool(size=2)
    with pool.acquire() as conn1:
        conn1.execute("INSERT INTO users(name, email) VALUES (?, ?)", ("P1", "p1@example.com"))
        conn1.commit()
    with pool.acquire() as conn2:
        count = conn2.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    pool.closeall()
    return {"count": count}


if __name__ == "__main__":
    print(run_demo())
