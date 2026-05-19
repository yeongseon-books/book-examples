from __future__ import annotations


class IrreversibleMigrationError(RuntimeError):
    pass


def reversible_change(change_kind: str) -> bool:
    return change_kind in {"add_nullable_column", "add_index", "create_table"}


def guarded_downgrade(change_kind: str) -> str:
    if reversible_change(change_kind):
        return "downgrade-applied"
    raise IrreversibleMigrationError(f"Irreversible change: {change_kind}")


# English mirror
if __name__ == "__main__":
    print(guarded_downgrade("add_nullable_column"))
