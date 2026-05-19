import json

from common import ep04_run_build_helper


def main() -> None:
    print(json.dumps(ep04_run_build_helper(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
