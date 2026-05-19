from ko.ep10_when_to_avoid_oop import Cart, CartItem, total_functional


def test_ep10_oop_vs_functional_total() -> None:
    oop_total = Cart([CartItem("a", 100, 2), CartItem("b", 50, 3)]).total()
    func_total = total_functional(
        [
            {"price": 100, "quantity": 2},
            {"price": 50, "quantity": 3},
        ]
    )
    assert oop_total == func_total == 350
