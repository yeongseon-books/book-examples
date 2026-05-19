from en.ep07_modules_packages import compute_pair


def test_compute_pair() -> None:
    assert compute_pair(9, 4) == (13, 5)
