from en import ep02_connection_cursor_lifecycle as ep


def test_ep02_connection_cursor_lifecycle():
    result = ep.run_demo()
    assert result["selected"] == 1
