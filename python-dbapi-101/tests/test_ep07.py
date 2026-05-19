from en import ep07_exceptions as ep


def test_ep07_exception_hierarchy():
    result = ep.run_demo()
    assert result["integrity"] == "caught"
    assert result["operational"] == "caught"
    assert result["database"] == "caught"
