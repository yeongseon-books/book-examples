from pathlib import Path
from ko.ep05_test_pyramid import analyze_test_pyramid


def test_ep05_pyramid_counts():
    text = Path("fixtures/ep05_test_index.txt").read_text(encoding="utf-8")
    assert analyze_test_pyramid(text) == {"unit": 1, "integration": 1, "e2e": 1}
