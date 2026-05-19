"""Tests for ep08 in Sqlalchemy 101."""

from ko import ep08_events_hybrid


def test_ep08_events_hybrid() -> None:
    """Test ep08 events hybrid."""
    assert ep08_events_hybrid.run() == "Alice Kim"
