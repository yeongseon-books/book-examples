"""Oop 101 - Episode 4: Inheritance."""

# pyright: reportImplicitOverride=false


class Employee:
    """Employee."""

    name: str
    base_salary: int

    def __init__(self, name: str, base_salary: int) -> None:
        self.name = name
        self.base_salary = base_salary

    def monthly_pay(self) -> int:
        """Monthly pay."""
        return self.base_salary


class SalesEmployee(Employee):
    """Sales employee."""

    sales_bonus: int

    def __init__(self, name: str, base_salary: int, sales_bonus: int) -> None:
        super().__init__(name, base_salary)
        self.sales_bonus = sales_bonus

    def monthly_pay(self) -> int:
        """Monthly pay."""
        return self.base_salary + self.sales_bonus


if __name__ == "__main__":
    employee = SalesEmployee("jina", 3000, 500)
    print(employee.monthly_pay())
