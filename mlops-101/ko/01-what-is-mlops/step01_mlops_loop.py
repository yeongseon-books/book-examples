from common import ProductionSystem


def run_overview() -> dict[str, float | str]:
    return ProductionSystem().bootstrap()


if __name__ == "__main__":
    print(run_overview())
