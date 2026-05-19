from en import ep06_row_factory as ep


def test_ep06_row_factory_and_dataclass():
    result = ep.run_demo()
    assert result["row_name"] == "Alice"
    assert result["record_type"] == "UserRecord"
