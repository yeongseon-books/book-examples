from ko.ep10_design_checklist import score_language


def test_ep10_design_checklist():
    out = score_language(7, 6, 7, 6)
    assert out["total"] == 26
    assert out["pass"] is True
