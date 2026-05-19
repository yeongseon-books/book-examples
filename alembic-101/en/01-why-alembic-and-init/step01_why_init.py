from __future__ import annotations

from common import ensure_version_table, get_version, make_memory_engine


def run_init_demo() -> dict[str, str]:
    engine = make_memory_engine()
    ensure_version_table(engine, version="0001_init")
    return {"mental_model": "git-for-schema", "version": get_version(engine)}


# English mirror
if __name__ == "__main__":
    print(run_init_demo())
