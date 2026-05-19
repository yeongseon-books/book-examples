from ko.ep05_polymorphism import CardPayment, PointPayment, checkout


def test_ep05_polymorphism_checkout() -> None:
    assert checkout(CardPayment(), 5000) == "card:5000"
    assert checkout(PointPayment(), 5000) == "point:5000"
