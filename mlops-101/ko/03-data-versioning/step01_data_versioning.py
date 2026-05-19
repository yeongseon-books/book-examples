import numpy as np

from common import DataVersionStore


def run_data_version_demo() -> tuple[str, str]:
    store = DataVersionStore()
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[1.0, 2.0], [3.0, 5.0]])
    return store.put(a), store.put(b)


if __name__ == "__main__":
    print(run_data_version_demo())
