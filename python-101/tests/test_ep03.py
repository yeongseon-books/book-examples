from en.ep03_strings_formatting import normalize_words


def test_normalize_words() -> None:
    assert normalize_words(" A, b, ,C ") == ["a", "b", "c"]
