from ko.ep01_portfolio_scorer import score_portfolio_project


def test_ep01_portfolio_scorer() -> None:
    score = score_portfolio_project(
        {"has_demo": True, "has_tests": True, "has_readme": True}
    )
    assert score == 60
