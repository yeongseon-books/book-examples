"""Tests for 04 dns in Computer Networks 101."""

from tests._loader import load_ko


def test_dns_recursive_path_and_cname() -> None:
    """Test dns recursive path and cname."""
    ep = load_ko("04-dns")
    assert ep.resolve("www.example.com") == "93.184.216.34"
    assert ep.recursive_path("www.example.com") == [
        ".",
        "com",
        "example.com",
        "www.example.com",
    ]
