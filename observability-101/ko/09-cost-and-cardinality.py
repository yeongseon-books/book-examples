from common import CardinalityAnalyzer


def run_demo() -> dict[str, object]:
    series = [
        ("http_requests_total", {"path": f"/p/{i}", "status": "200"})
        for i in range(1101)
    ]
    return CardinalityAnalyzer.analyze(series, threshold=1000)
