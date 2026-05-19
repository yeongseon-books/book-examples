from en.ep03_title_structure_linter import analyze


def test_ep03_heading_rules():
    good = analyze("fixtures/ep03_good.md")
    bad = analyze("fixtures/ep03_bad.md")
    assert good["has_h1"] and good["no_skipped_levels"]
    assert not bad["has_h1"] or not bad["no_skipped_levels"]
