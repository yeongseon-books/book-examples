"""Tests for ep01 in Operating Systems 101."""

from common import ep01_os_info


def test_ep01_os_info_has_required_keys():
    """Test ep01 os info has required keys."""
    data = ep01_os_info()
    assert "platform" in data
    assert "cpu_count" in data
    assert isinstance(data["cpu_count"], int | type(None))
