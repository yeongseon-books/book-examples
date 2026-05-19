from __future__ import annotations


def plan_deploy(change_kind: str) -> list[str]:
    if change_kind == "add_column":
        return ["migration", "deploy"]
    if change_kind == "drop_column":
        return ["deploy", "migration"]
    return ["migration", "deploy", "verify"]


def blue_green_compatible(schema_stage: str) -> bool:
    return schema_stage in {"expand", "dual-write", "read-new"}


if __name__ == "__main__":
    print(plan_deploy("add_column"))
