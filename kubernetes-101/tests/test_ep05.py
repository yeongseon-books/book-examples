"""Tests for ep05 in Kubernetes 101."""

from pathlib import Path

from common import IngressRouter, ManifestParser


def test_ep05_ingress_routes_api_path():
    """Test ep05 ingress routes api path."""
    ing = ManifestParser().parse(Path("ko/05-ingress/ingress.yaml").read_text())[0]
    assert IngressRouter().route(ing, "example.com", "/api/users") == "api"
    assert IngressRouter().route(ing, "example.com", "/home") == "web"
