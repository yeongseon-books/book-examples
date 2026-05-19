from en.ep02_reader_profile import analyze


def test_ep02_profile_advanced():
    res = analyze("fixtures/ep02_profile.md")
    assert res["audience"] == "advanced"
