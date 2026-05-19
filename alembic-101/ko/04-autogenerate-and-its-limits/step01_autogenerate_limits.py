from __future__ import annotations


def classify_autogen_change(change: dict[str, str]) -> str:
    kind = change["kind"]
    if kind in {"add_table", "drop_table", "add_column", "drop_column"}:
        return "safe-auto"
    if kind in {"rename_table", "rename_column"}:
        return "manual-required"
    return "review-required"


def compare_options() -> dict[str, bool]:
    return {"compare_type": True, "compare_server_default": True}


if __name__ == "__main__":
    print(classify_autogen_change({"kind": "rename_column"}))
