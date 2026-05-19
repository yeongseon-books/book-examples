"""Tests for ep02 in Serverless 101."""

from common import *
from en.ep02_faas_runtime import run_demo


def test_ep02():
    """Test ep02."""
    out = run_demo()
    assert out["echo"]["msg"] == "hi"
