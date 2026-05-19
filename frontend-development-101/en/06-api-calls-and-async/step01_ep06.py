"""Frontend Development 101 - Episode 1: Ep06."""

from __future__ import annotations

from common import JSAnalyzer, MockFetch

JS_SAMPLE = """async function load(){ const r = await fetch('/api/users'); return await r.json(); }"""


def run_demo() -> dict[str, object]:
    """Run demo."""
    mock = MockFetch({"/api/users": {"status": "success", "data": [{"id": 1}]}})
    js = JSAnalyzer(JS_SAMPLE)
    return {
        "result": mock.get("/api/users"),
        "async_patterns": js.async_patterns(),
    }
