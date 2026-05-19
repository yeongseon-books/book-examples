from en import ep03_fetch_patterns as ep


def test_ep03_fetch_patterns_and_executemany():
    result = ep.run_demo()
    assert result["first"] == "Alice"
    assert result["many"] == ["Alice", "Bob"]
    assert result["count"] == 5
