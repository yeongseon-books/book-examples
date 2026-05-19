from ko.ep04_inheritance import Employee, SalesEmployee


def test_ep04_inheritance_override() -> None:
    assert Employee("a", 1000).monthly_pay() == 1000
    assert SalesEmployee("b", 1000, 300).monthly_pay() == 1300
