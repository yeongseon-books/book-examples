"""Tests for ep06 in Information Security 101."""

from common import SQLInjectionDetector, XSSDetector


def test_injection_and_xss_detectors():
    """Test injection and xss detectors."""
    assert SQLInjectionDetector().is_suspicious("' OR 1=1 --")
    assert XSSDetector().is_suspicious("<script>alert(1)</script>")
