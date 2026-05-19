"""Database Systems 101 - Episode 5: Transactions and acid."""

from __future__ import annotations

import sqlite3
from pathlib import Path


def init_bank(db_path: Path) -> None:
    """Init bank."""
    with sqlite3.connect(db_path) as db:
        db.executescript(
            """
            DROP TABLE IF EXISTS accounts;
            CREATE TABLE accounts(id INTEGER PRIMARY KEY, owner TEXT, balance INTEGER NOT NULL CHECK(balance >= 0));
            INSERT INTO accounts VALUES (1,'Alice',1000),(2,'Bob',1000);
            """
        )


def transfer(
    db_path: Path, src: int, dst: int, amount: int, fail_midway: bool = False
) -> None:
    """Transfer."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    with sqlite3.connect(db_path) as db:
        try:
            db.execute("BEGIN")
            src_update = db.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, src)
            )
            if src_update.rowcount != 1:
                raise ValueError("source account not found")
            if fail_midway:
                raise RuntimeError("simulated failure")
            dst_update = db.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, dst)
            )
            if dst_update.rowcount != 1:
                raise ValueError("destination account not found")
            db.execute("COMMIT")
        except Exception:
            db.execute("ROLLBACK")
            raise


class ToyWAL:
    """Toy w a l."""

    def __init__(self):
        self.state = {"Alice": 1000, "Bob": 1000}
        self.log: list[tuple[str, str, int]] = []
        self._applied_pos = 0

    def append_transfer(self, src: str, dst: str, amount: int) -> None:
        """Append transfer."""
        self.log.append((src, dst, amount))

    def apply(self) -> None:
        """Apply."""
        for src, dst, amount in self.log[self._applied_pos :]:
            self.state[src] -= amount
            self.state[dst] += amount
        self._applied_pos = len(self.log)


def balances(db_path: Path) -> dict[str, int]:
    """Balances."""
    with sqlite3.connect(db_path) as db:
        return {
            owner: bal
            for owner, bal in db.execute(
                "SELECT owner, balance FROM accounts ORDER BY id"
            )
        }


if __name__ == "__main__":
    p = Path("tmp_ep05.db")
    init_bank(p)
    transfer(p, 1, 2, 100)
    print(balances(p))
