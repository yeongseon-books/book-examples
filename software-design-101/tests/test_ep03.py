"""Tests for ep03 in Software Design 101."""

import ko.ep03_modules_boundaries as ep03


def test_ep03_public_boundary() -> None:
    """Test ep03 public boundary."""
    assert ep03.can_import("public_api", ep03)
    assert not ep03.can_import("_internal_helper", ep03)
