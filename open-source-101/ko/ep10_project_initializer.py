from __future__ import annotations

from common import (
    initialize_python_project,
)


def run_example() -> object:
    path = initialize_python_project("demo_pkg")
    return str(path)


if __name__ == "__main__":
    print(run_example())
