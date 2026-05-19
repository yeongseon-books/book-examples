"""Python 101 - Episode 10: Stdlib tour."""

import itertools
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


def stdlib_snapshot(words: list[str]) -> dict[str, object]:
    """Stdlib snapshot."""
    now = datetime(2024, 1, 1, 12, 0, 0)
    counts = Counter(words)
    combos = list(itertools.islice(itertools.permutations([1, 2, 3], 2), 3))
    path_name = Path("demo.txt").suffix
    payload = json.dumps({"words": words}, ensure_ascii=False)
    return {
        "iso_time": now.isoformat(),
        "top_word": counts.most_common(1)[0],
        "combos": combos,
        "suffix": path_name,
        "json": payload,
    }


def main() -> None:
    """Main."""
    print(stdlib_snapshot(["a", "b", "a"]))


if __name__ == "__main__":
    main()
