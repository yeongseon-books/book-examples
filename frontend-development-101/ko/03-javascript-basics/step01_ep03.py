from __future__ import annotations

from common import JSAnalyzer

JS_SAMPLE = """const todos = []; let count = 0; function App() { return todos.length + count; }"""


def run_demo() -> dict[str, object]:
    analyzer = JSAnalyzer(JS_SAMPLE)
    return {
        "decls": analyzer.declaration_counts(),
        "components": analyzer.component_names(),
    }
