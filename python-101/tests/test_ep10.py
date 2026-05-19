from en.ep10_stdlib_tour import stdlib_snapshot


def test_stdlib_snapshot() -> None:
    snap = stdlib_snapshot(["x", "x", "y"])
    assert snap["top_word"] == ("x", 2)
    assert snap["suffix"] == ".txt"
