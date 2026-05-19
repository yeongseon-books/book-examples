from en import ep09_async_patterns as ep


def test_ep09_async_pattern_count_users():
    result = ep.run_demo()
    assert result["count"] >= 2
