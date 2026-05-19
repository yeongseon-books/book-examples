"""Python 101 - Episode 1: Hello world."""

import platform
import sys


def get_runtime_info() -> dict[str, str]:
    """Get runtime info."""
    return {"python_version": sys.version.split()[0], "platform": platform.system()}


def main() -> None:
    """Main."""
    print("안녕하세요, Python 101!")
    info = get_runtime_info()
    print(f"Python: {info['python_version']}")
    print(f"Platform: {info['platform']}")


if __name__ == "__main__":
    main()
