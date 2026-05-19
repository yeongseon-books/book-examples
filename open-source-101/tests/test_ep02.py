from common import (
    is_license_compatible,
)
from en.ep02_license_compatibility import run_example as run_en
from ko.ep02_license_compatibility import run_example as run_ko


def test_ep02_behavior():
    assert run_ko() is True
    assert run_en() is True
    assert is_license_compatible("Apache-2.0", "GPL-3.0-only") is False
