import json

from common import ep01_detect_package_vs_module


def main() -> None:
    result = ep01_detect_package_vs_module("sample_pkg")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
