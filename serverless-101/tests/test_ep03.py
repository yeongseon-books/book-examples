"""Tests for ep03 in Serverless 101."""

from common import *
from en.ep03_event_router import run_demo


def test_ep03():
    """Test ep03."""
    out = run_demo()
    assert out["kind"] == "http" and out["path"] == "/ping"
