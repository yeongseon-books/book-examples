import json
from pathlib import Path

from common import ep10_generate_template


def main() -> None:
    result = ep10_generate_template(Path("generated"), project_name="episode10_pkg")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
