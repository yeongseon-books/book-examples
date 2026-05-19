from en import ep01_pep249_conformance as ep


def test_ep01_pep249_constants():
    result = ep.run_demo()
    assert result["apilevel"] == "2.0"
    assert result["paramstyle"] == "qmark"
    assert isinstance(result["threadsafety"], int)
