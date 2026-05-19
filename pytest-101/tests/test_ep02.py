from en.ep02_parser import parse_key_value


def test_ep02_parse_key_value_basic_assertion():
    parsed = parse_key_value("name=pytest, level=101")
    assert parsed == {"name": "pytest", "level": "101"}


def test_ep02_parse_key_value_invalid_input_raises():
    import pytest

    with pytest.raises(ValueError):
        parse_key_value("missing-separator")
