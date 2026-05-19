from en.ep03_where import run_demo


def test_ep03_where_predicates():
    names = run_demo()
    assert names == ["Charlie", "Evan", "Fiona"]
