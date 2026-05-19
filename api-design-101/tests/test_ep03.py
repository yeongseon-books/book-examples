"""Tests for ep03 in Api Design 101."""

from __future__ import annotations

from .helpers import client_for, load_module


def test_ep03_nested_resource_url() -> None:
    """Test ep03 nested resource url."""
    mod = load_module("ko/03-resource-design/step01_resource_url.py", "ep03_ko")
    app = mod.build_app()
    c = client_for(app)
    assert c.get("/users/42/orders/9").json()["status"] == "paid"
    assert c.get("/users/99/orders/9").status_code == 404
