"""Mlops 101 - Episode 1: Production system."""

from common import ProductionSystem


def run_production_demo() -> dict[str, float | str]:
    """Run production demo."""
    return ProductionSystem().bootstrap()


if __name__ == "__main__":
    print(run_production_demo())
