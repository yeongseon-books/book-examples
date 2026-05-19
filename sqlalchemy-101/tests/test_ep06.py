from ko import ep06_relationships


def test_ep06_relationships() -> None:
    post_count, tag_count = ep06_relationships.run()
    assert post_count == 1
    assert tag_count == 1
