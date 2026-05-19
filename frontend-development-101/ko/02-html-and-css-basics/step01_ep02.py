from __future__ import annotations

from common import CSSAnalyzer

HTML_SAMPLE = """<main><article class="card">x</article></main>"""
CSS_SAMPLE = """:root { --color-primary: #1d72ff; } .card { color: var(--color-primary); } .unused { color: #fff; }"""


def run_demo() -> dict[str, object]:
    analyzer = CSSAnalyzer(CSS_SAMPLE)
    return {
        "specificity": analyzer.selector_specificity(".card"),
        "unused": analyzer.unused_selectors(HTML_SAMPLE),
        "token_violations": analyzer.enforce_tokens(),
    }
