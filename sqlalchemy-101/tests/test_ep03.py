from ko import ep03_core_crud


def test_ep03_core_crud() -> None:
    result = ep03_core_crud.run()
    assert result["before"] == "alice"
    assert result["after"] == "alice-updated"
    assert result["count"] == "0"
