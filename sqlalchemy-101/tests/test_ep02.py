from ko import ep02_core_metadata


def test_ep02_core_metadata() -> None:
    assert ep02_core_metadata.run() == ["products"]
