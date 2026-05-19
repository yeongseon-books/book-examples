"""Tests for ep01 in Open Source 101."""

from pathlib import Path

from common import (
    detect_spdx_license,
)
from en.ep01_license_detector import run_example as run_en
from ko.ep01_license_detector import run_example as run_ko


def test_ep01_behavior():
    """Test ep01 behavior."""
    assert run_ko() == "MIT"
    assert run_en() == "MIT"
    apache = Path("fixtures/LICENSE_APACHE.txt").read_text(encoding="utf-8")
    assert detect_spdx_license(apache) == "Apache-2.0"
