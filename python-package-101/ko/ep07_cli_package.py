import json
from common import ep07_run_cli


def main() -> None:
    code, out = ep07_run_cli(["world"])
    print(json.dumps({"returncode": code, "stdout": out}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
