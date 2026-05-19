"""Python Package 101 - Episode 3: Dependency parser."""

import json
from pathlib import Path

from common import ep03_parse_dependencies


def main() -> None:
    """Main."""
    result = ep03_parse_dependencies(Path("fixtures/sample_pyproject.toml"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
