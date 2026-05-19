"""Python Package 101 - Episode 9: Docstring extractor."""

import json
from pathlib import Path

from common import ep09_extract_docstrings


def main() -> None:
    """Main."""
    result = ep09_extract_docstrings(Path("fixtures/sample_module.py"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
