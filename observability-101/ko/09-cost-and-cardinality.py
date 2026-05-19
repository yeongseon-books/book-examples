"""Observability 101 - Episode 9: Cost and cardinality."""

from common import CardinalityAnalyzer


def run_demo() -> dict[str, object]:
    """Run demo."""
    series = [
        ("http_requests_total", {"path": f"/p/{i}", "status": "200"})
        for i in range(1101)
    ]
    return CardinalityAnalyzer.analyze(series, threshold=1000)
