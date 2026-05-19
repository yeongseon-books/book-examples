"""Tests for ep06 in Serverless 101."""

from common import *
from en.ep06_state_idempotency import run_demo


def test_ep06():
    """Test ep06."""
    out = run_demo()
    assert out["first_seen"] is False and out["second_seen"] is True
