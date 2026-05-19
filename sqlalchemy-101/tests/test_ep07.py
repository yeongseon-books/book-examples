from ko import ep07_loading_strategies


def test_ep07_loading_strategies() -> None:
    result = ep07_loading_strategies.run()
    assert result["naive_posts"] == 4
    assert result["selectin_users"] == 2
    assert result["joined_users"] == 2
