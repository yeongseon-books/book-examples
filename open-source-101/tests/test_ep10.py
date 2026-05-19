"""Tests for ep10 in Open Source 101."""

from pathlib import Path

from common import (
    initialize_python_project,
)
from en.ep10_project_initializer import run_example as run_en
from ko.ep10_project_initializer import run_example as run_ko


def test_ep10_behavior():
    """Test ep10 behavior."""
    created_ko = Path(run_ko())
    created_en = Path(run_en())
    assert (created_ko / "demo_pkg" / "core.py").exists()
    assert (created_en / "pyproject.toml").exists()
    path = initialize_python_project("another_pkg")
    assert (path / "another_pkg" / "__init__.py").exists()
