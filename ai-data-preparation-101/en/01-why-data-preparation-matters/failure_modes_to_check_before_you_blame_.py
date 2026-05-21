"""Generated from book-content article."""

def compare_reports(prev: dict, curr: dict) -> dict[str, float]:
    return {
        "duplicate_ratio_delta": curr["duplicate_ratio"] - prev["duplicate_ratio"],
        "p99_length_delta": curr["p99_length"] - prev["p99_length"],
        "null_ratio_delta": curr["null_ratio"] - prev["null_ratio"],
    }

prev = {"duplicate_ratio": 0.04, "p99_length": 820, "null_ratio": 0.01}
curr = {"duplicate_ratio": 0.13, "p99_length": 1410, "null_ratio": 0.03}
print(compare_reports(prev, curr))
