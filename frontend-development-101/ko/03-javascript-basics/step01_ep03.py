"""Frontend Development 101 - 3편: javascript basics 예제."""

from __future__ import annotations

from common import JSAnalyzer

JS_SAMPLE = """const todos = []; let count = 0; function App() { return todos.length + count; }"""


def run_demo() -> dict[str, object]:
    """데모를 실행합니다."""
    analyzer = JSAnalyzer(JS_SAMPLE)
    return {
        "decls": analyzer.declaration_counts(),
        "components": analyzer.component_names(),
    }
