import pytest


@pytest.fixture
def sample_numbers() -> tuple[int, int]:
    return 7, 5


@pytest.fixture(scope="module")
def module_tag() -> str:
    return "pytest-101"
