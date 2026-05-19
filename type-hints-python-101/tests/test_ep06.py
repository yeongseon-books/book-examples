from ko.ep06_protocol_structural import pick_smallest


def test_ep06_protocol_structural_typing() -> None:
    assert pick_smallest([3, 1, 2]) == 1
