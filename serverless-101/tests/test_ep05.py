"""Tests for ep05 in Serverless 101."""

from common import *
from en.ep05_autoscaling import run_demo


def test_ep05():
    """Test ep05."""
    out = run_demo()
    assert out == {"active": 3, "queued": 2, "dropped": 3}
