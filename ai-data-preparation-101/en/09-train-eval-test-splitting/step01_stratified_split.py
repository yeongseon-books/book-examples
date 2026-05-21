"""Ai Data Preparation 101 - Episode 9: train eval test splitting example."""

from collections import defaultdict


def run() -> dict[str, dict[str, int]]:
    """Run."""
    rows = [
        {"id": "a", "label": "pos"},
        {"id": "b", "label": "pos"},
        {"id": "c", "label": "pos"},
        {"id": "d", "label": "neg"},
        {"id": "e", "label": "neg"},
        {"id": "f", "label": "neg"},
    ]
    by_label: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_label[row["label"]].append(row)
    train: list[dict[str, str]] = []
    test: list[dict[str, str]] = []
    for items in by_label.values():
        train.extend(items[:2])
        test.extend(items[2:])
    return {
        "train": {
            "pos": sum(1 for r in train if r["label"] == "pos"),
            "neg": sum(1 for r in train if r["label"] == "neg"),
        },
        "test": {
            "pos": sum(1 for r in test if r["label"] == "pos"),
            "neg": sum(1 for r in test if r["label"] == "neg"),
        },
    }


if __name__ == "__main__":
    print(run())
