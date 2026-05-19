import json
from pathlib import Path

from common import ep08_count_annotations


def main() -> None:
    result = ep08_count_annotations(Path("fixtures/sample_module.py"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
