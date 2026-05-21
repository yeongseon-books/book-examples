"""Generated from book-content article."""

import json
from pathlib import Path
import hashlib

def assert_snapshot(name: str, actual: dict, snapshot_dir: Path = Path("tests/snapshots")):
    """Compare against a saved snapshot."""
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    snapshot_file = snapshot_dir / f"{name}.json"

    actual_str = json.dumps(actual, sort_keys=True, indent=2)

    if not snapshot_file.exists():
        snapshot_file.write_text(actual_str)
        print(f"snapshot created: {snapshot_file}")
        return

    expected_str = snapshot_file.read_text()
    if actual_str != expected_str:
        actual_hash = hashlib.sha256(actual_str.encode()).hexdigest()[:8]
        expected_hash = hashlib.sha256(expected_str.encode()).hexdigest()[:8]
        raise AssertionError(
            f"snapshot mismatch for {name}\n"
            f"  expected: {expected_hash}\n"
            f"  actual:   {actual_hash}\n"
        )

def test_classification_snapshot(deterministic_agent):
    """The classification task's output does not change."""
    result = deterministic_agent.classify("This product is amazing!")
    assert_snapshot("positive_review_classification", result)
