# regression/check_thresholds.py
import json
import sys

from .thresholds import FAIL_POLICY, THRESHOLDS


def check(report_path: str) -> int:
    with open(report_path) as f:
        report = json.load(f)

    failures = []
    for metric, threshold in THRESHOLDS.items():
        if metric not in report:
            continue
        score = report[metric]
        if score < threshold:
            failures.append(f"{metric}: {score:.3f} < {threshold}")

    if FAIL_POLICY == "any" and failures:
        print("FAIL — threshold violations:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("PASS — all metrics above threshold")
    return 0

if __name__ == "__main__":
    sys.exit(check(sys.argv[1]))
