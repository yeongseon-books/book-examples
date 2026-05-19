from pathlib import Path
import json
from common import ep09_extract_docstrings


def main() -> None:
    result = ep09_extract_docstrings(Path("fixtures/sample_module.py"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
