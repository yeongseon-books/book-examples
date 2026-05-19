from en.ep06_subquery import run_demo


def test_ep06_subquery_variants():
    out = run_demo()
    assert out["scalar"] == "Alice"
    assert out["in_subquery"] == ["Bob", "Fiona"]
    assert out["exists"] == ["Fiona"]
