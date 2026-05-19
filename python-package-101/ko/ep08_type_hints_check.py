"""Python Package 101 - Episode 8: Type hints check."""

import json
from pathlib import Path

from common import ep08_count_annotations


def main() -> None:
    """Main."""
    result = ep08_count_annotations(Path("fixtures/sample_module.py"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
