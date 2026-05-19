"""Pytest configuration and fixtures for Pytest 101."""

import pytest


@pytest.fixture
def sample_numbers() -> tuple[int, int]:
    """Sample numbers."""
    return 7, 5


@pytest.fixture(scope="module")
def module_tag() -> str:
    """Module tag."""
    return "pytest-101"
