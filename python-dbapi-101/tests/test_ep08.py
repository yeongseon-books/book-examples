from en import ep08_connection_pool as ep


def test_ep08_connection_pool_basic_usage():
    result = ep.run_demo()
    assert result["count"] >= 0
