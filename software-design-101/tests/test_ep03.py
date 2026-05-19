import ko.ep03_modules_boundaries as ep03


def test_ep03_public_boundary() -> None:
    assert ep03.can_import("public_api", ep03)
    assert not ep03.can_import("_internal_helper", ep03)
