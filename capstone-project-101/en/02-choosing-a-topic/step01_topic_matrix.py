from __future__ import annotations

from common import best_by_total


def run() -> dict[str, object]:
    score = {
        "schedule_checker": [4, 5, 4],
        "mood_diary": [3, 4, 5],
        "campus_map": [4, 3, 3],
    }
    pick, total = best_by_total(score)
    return {"pick": pick, "total": total}


if __name__ == "__main__":
    print(run())
