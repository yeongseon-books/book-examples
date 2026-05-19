"""Frontend Development 101 - Episode 1: Ep01."""

from __future__ import annotations

from common import HTMLAnalyzer

HTML_SAMPLE = """<!doctype html><html lang="ko"><body><header><main><h1>Hi</h1><button id="b">go</button><img src="a.png" alt="설명"></main><footer></footer></body></html>"""


def run_demo() -> dict[str, object]:
    """Run demo."""
    analyzer = HTMLAnalyzer(HTML_SAMPLE)
    return {
        "semantic_ok": analyzer.has_semantic_tags({"header", "main", "footer"}),
        "missing_alt": analyzer.missing_alt_images(),
    }
