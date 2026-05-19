from __future__ import annotations


def render_upgrade_sql(revision_from: str, revision_to: str) -> str:
    return "\n".join([
        "BEGIN;",
        f"-- Running upgrade {revision_from} -> {revision_to}",
        "ALTER TABLE users ADD COLUMN phone VARCHAR(20);",
        "UPDATE alembic_version SET version_num='" + revision_to + "';",
        "COMMIT;",
    ])


def requires_batch(dialect_name: str) -> bool:
    return dialect_name == "sqlite"


if __name__ == "__main__":
    print(render_upgrade_sql("a1", "b1"))
