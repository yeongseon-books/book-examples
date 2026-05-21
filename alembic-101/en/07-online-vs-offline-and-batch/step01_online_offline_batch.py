"""Alembic 101 - Episode 7: online vs offline and batch example."""

from __future__ import annotations


def render_upgrade_sql(revision_from: str, revision_to: str) -> str:
    """Render upgrade sql."""
    return "\n".join(
        [
            "BEGIN;",
            f"-- Running upgrade {revision_from} -> {revision_to}",
            "ALTER TABLE users ADD COLUMN phone VARCHAR(20);",
            "UPDATE alembic_version SET version_num='" + revision_to + "';",
            "COMMIT;",
        ]
    )


def requires_batch(dialect_name: str) -> bool:
    """Requires batch."""
    return dialect_name == "sqlite"


# English mirror
if __name__ == "__main__":
    print(render_upgrade_sql("a1", "b1"))
