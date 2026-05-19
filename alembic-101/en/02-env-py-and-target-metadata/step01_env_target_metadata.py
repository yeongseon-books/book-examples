from __future__ import annotations

import os


def resolve_db_url(default_url: str) -> str:
    return os.environ.get("DATABASE_URL", default_url)


def build_env_config(default_url: str = "sqlite:///./app.db") -> dict[str, object]:
    url = resolve_db_url(default_url)
    return {
        "sqlalchemy.url": url,
        "target_metadata": "Base.metadata",
        "render_as_batch": url.startswith("sqlite"),
    }


# English mirror
if __name__ == "__main__":
    print(build_env_config())
