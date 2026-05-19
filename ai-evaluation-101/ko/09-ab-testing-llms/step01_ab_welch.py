import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import welch_t_test


def run() -> dict[str, float | bool]:
    model_a_scores = [0.75, 0.79, 0.8, 0.77, 0.81, 0.76]
    model_b_scores = [0.7, 0.72, 0.71, 0.69, 0.73, 0.7]
    t_value, p_value = welch_t_test(model_a_scores, model_b_scores)
    return {
        "t_value": t_value,
        "p_value": p_value,
        "is_better": p_value < 0.05 and t_value > 0,
    }


if __name__ == "__main__":
    print(run())
