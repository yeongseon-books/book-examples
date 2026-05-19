"""Tests for ep07 in Sqlalchemy 101."""

from ko import ep07_loading_strategies


def test_ep07_loading_strategies() -> None:
    """Test ep07 loading strategies."""
    result = ep07_loading_strategies.run()
    assert result["naive_posts"] == 4
    assert result["selectin_users"] == 2
    assert result["joined_users"] == 2
