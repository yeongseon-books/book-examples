from pathlib import Path

from en.ep02_html_css_js import run


def test_ep02_html_structure_validator():
    fixture = Path(__file__).resolve().parent.parent / "fixtures" / "index.html"
    out = run(str(fixture))
    assert out["h1_count"] == 1
    assert out["has_charset"] is True
    assert out["has_viewport"] is True
