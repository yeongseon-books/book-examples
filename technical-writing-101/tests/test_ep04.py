from en.ep04_concept_linter import analyze


def test_ep04_what_before_how():
    assert analyze("fixtures/ep04_good.md")["what_before_how"]
    assert not analyze("fixtures/ep04_bad.md")["what_before_how"]
