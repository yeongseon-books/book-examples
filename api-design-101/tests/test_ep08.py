"""Tests for ep08 in Api Design 101."""

from __future__ import annotations

from .helpers import client_for, load_module


def test_ep08_openapi_generated() -> None:
    """Test ep08 openapi generated."""
    mod = load_module("ko/08-openapi-and-swagger/step01_openapi_contract.py", "ep08_ko")
    app = mod.build_app()
    c = client_for(app)
    spec = c.get("/openapi.json").json()
    assert spec["openapi"].startswith("3.")
    assert "/users/{uid}" in spec["paths"]
