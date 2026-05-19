import json
from pathlib import Path

from common import ep02_validate_project_structure


def main() -> None:
    result = ep02_validate_project_structure(Path("."))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
