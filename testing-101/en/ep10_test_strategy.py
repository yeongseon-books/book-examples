from pathlib import Path


def analyze_test_pyramid(root: str = "tests") -> dict:
    counts = {"unit": 0, "integration": 0, "e2e": 0}
    for p in Path(root).glob("test_*.py"):
        name = p.name.lower()
        if "integration" in name or "ep03" in name:
            counts["integration"] += 1
        elif "e2e" in name or "ep04" in name:
            counts["e2e"] += 1
        else:
            counts["unit"] += 1
    return counts


def suggest_gap(counts: dict) -> str:
    if counts["unit"] < counts["integration"]:
        return "Increase unit tests"
    if counts["integration"] < 1:
        return "Add at least one integration test"
    if counts["e2e"] < 1:
        return "Add at least one end-to-end test"
    return "Balanced enough for current stage"
