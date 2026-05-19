from common import (
    score_portfolio,
)
from en.ep09_portfolio_scorer import run_example as run_en
from ko.ep09_portfolio_scorer import run_example as run_ko


def test_ep09_behavior():
    score = run_ko()
    assert score == 150
    assert run_en() == 150
    assert score_portfolio("[]") == 0
