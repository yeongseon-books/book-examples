"""Tests for ep02 in Api Design 101."""

from __future__ import annotations

from .helpers import client_for, load_module


def test_ep02_rest_method_url_pair() -> None:
    """Test ep02 rest method url pair."""
    mod = load_module("ko/02-rest-basics/step01_rest_constraints.py", "ep02_ko")
    app = mod.build_app()
    c = client_for(app)
    assert c.get("/users/42").status_code == 200
    assert c.post("/users").status_code == 201
