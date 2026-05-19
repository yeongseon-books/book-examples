"""Tests for ep10 in Software Design 101."""

from ko.ep05_interfaces_abstraction import MockGateway
from ko.ep10_small_design_practice import UrlRepository, UrlShortenerService


def test_ep10_tiny_url_shortener() -> None:
    """Test ep10 tiny url shortener."""
    repo = UrlRepository()
    gateway = MockGateway()
    service = UrlShortenerService(repo, gateway)
    code = service.create("https://example.com/page", amount=100)
    assert service.resolve(code) == "https://example.com/page"
    assert gateway.calls == [100]
