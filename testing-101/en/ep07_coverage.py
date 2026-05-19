"""Testing 101 - Episode 7: Coverage."""

from coverage import Coverage


def shipping_fee(total: float, member: bool) -> int:
    """Shipping fee."""
    if total >= 50000:
        return 0
    if member:
        return 1500
    return 3000


def report_coverage_for_module(module_path: str) -> float:
    """Report coverage for module."""
    cov = Coverage(source=[module_path.rsplit("/", 1)[0] or "."])
    cov.start()
    shipping_fee(10000, True)
    shipping_fee(70000, False)
    cov.stop()
    cov.save()
    _, statements, _, missing, _ = cov.analysis2(module_path)
    return round((len(statements) - len(missing)) / len(statements) * 100, 2)
