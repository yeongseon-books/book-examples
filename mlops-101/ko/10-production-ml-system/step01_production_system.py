from common import ProductionSystem


def run_production_demo() -> dict[str, float | str]:
    return ProductionSystem().bootstrap()


if __name__ == "__main__":
    print(run_production_demo())
