"""Tests for ep01 in Oop 101."""

from ko.ep01_what_is_oop import Thermostat, run_demo


def test_ep01_heat_needed() -> None:
    """Test ep01 heat needed."""
    assert Thermostat(target=20, current=18).heat_needed() is True
    assert run_demo() == "heating"
