"""Tests for ep04 in Serverless 101."""

from common import *
from en.ep04_cold_start import run_demo


def test_ep04():
    """Test ep04."""
    out = run_demo()
    assert out["first"]["cold_start"] is True and out["second"]["cold_start"] is False
