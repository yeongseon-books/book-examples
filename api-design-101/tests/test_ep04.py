"""Tests for ep04 in Api Design 101."""

from __future__ import annotations

from .helpers import client_for, load_module


def test_ep04_method_status_mapping() -> None:
    """Test ep04 method status mapping."""
    mod = load_module(
        "ko/04-http-methods-and-status/step01_method_status.py", "ep04_ko"
    )
    app = mod.build_app()
    c = client_for(app)
    assert c.get("/users/42").status_code == 200
    assert c.delete("/users/42").status_code == 204
