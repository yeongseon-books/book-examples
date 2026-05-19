from common import risk_score


def test_risk_score():
    assert risk_score(3, 5) == 15
