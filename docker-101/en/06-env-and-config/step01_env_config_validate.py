"""Docker 101 - Episode 1: Env config validate."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import EnvParser

# English note: offline validation example.


def run() -> dict[str, object]:
    """Run."""
    env_content = """LOG_LEVEL=INFO
DB_URL=postgres://db/app
"""
    parsed = EnvParser().parse_env_file(env_content)
    required = ["LOG_LEVEL", "DB_URL"]
    missing = [k for k in required if k not in parsed]
    return {"success": len(missing) == 0, "env": parsed, "missing": missing}


if __name__ == "__main__":
    print(run())
