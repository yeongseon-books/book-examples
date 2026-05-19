"""Python Dbapi 101 - Episode 1: Pep249 conformance."""

import sqlite3


def run_demo() -> dict[str, object]:
    """Run demo."""
    return {
        "module": sqlite3.__name__,
        "apilevel": sqlite3.apilevel,
        "threadsafety": sqlite3.threadsafety,
        "paramstyle": sqlite3.paramstyle,
    }


if __name__ == "__main__":
    print(run_demo())
