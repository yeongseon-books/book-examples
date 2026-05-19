"""Mlops 101 - Episode 1: Mlops loop."""

from common import ProductionSystem


def run_overview() -> dict[str, float | str]:
    """Run overview."""
    return ProductionSystem().bootstrap()


if __name__ == "__main__":
    print(run_overview())
