import pytest
from en.ep05_validator import is_valid_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("Aa123456", True, id="valid-mixed"),
        pytest.param("short1A", False, id="too-short"),
        pytest.param("lowercase123", False, id="no-uppercase"),
        pytest.param("UPPERCASE123", False, id="no-lowercase"),
        pytest.param("NoDigitsHere", False, id="no-digits"),
    ],
)
def test_ep05_password_validator_parametrized(password, expected):
    assert is_valid_password(password) is expected
