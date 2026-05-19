"""Tests for 03 runtime in Containers 101."""

from ko import _03_runtime as ep


def test_valid_oci_subset_passes():
    """Test valid oci subset passes."""
    cfg = {
        "process": {"args": ["python", "app.py"]},
        "root": {"path": "/rootfs"},
        "mounts": [{"destination": "/proc", "type": "proc", "source": "proc"}],
    }
    assert ep.validate_oci_config(cfg) == []


def test_missing_sections_fail():
    """Test missing sections fail."""
    errors = ep.validate_oci_config({})
    assert "process is required" in errors
    assert "root is required" in errors
