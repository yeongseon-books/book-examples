import json
from pathlib import Path

from common import ep05_validate_metadata


def main() -> None:
    result = ep05_validate_metadata(Path("fixtures/sample_pyproject.toml"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
