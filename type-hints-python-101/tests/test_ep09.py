from ko.ep09_pydantic_v2 import safe_create_product


def test_ep09_pydantic_validation() -> None:
    ok, payload = safe_create_product({'name': 'book', 'price': 10.0, 'quantity': 2})
    assert ok is True
    assert payload.startswith('book:10.0:2')
    bad_ok, bad_payload = safe_create_product({'name': 'book', 'price': -1.0, 'quantity': 2})
    assert bad_ok is False
    assert 'validation error' in bad_payload.lower()
