from ko import ep01_engine_connection


def test_ep01_engine_connection() -> None:
    assert ep01_engine_connection.run() == 1
