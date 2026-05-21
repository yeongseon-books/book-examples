"""Generated from book-content article."""

def harvest_failures_to_regression_set(failed_traces: list[dict], regression_path: str):
    new_cases = [
        {
            "input": t["input"],
            "expected": t.get("ground_truth") or "TBD - human label needed",
            "category": t["category"],
            "source": "production_failure",
            "harvested_at": datetime.utcnow().isoformat(),
        }
        for t in failed_traces
    ]
    with open(regression_path, "a") as f:
        for case in new_cases:
            f.write(json.dumps(case) + "\n")
