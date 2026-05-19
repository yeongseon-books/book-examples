"""Testing 101 - Episode 9: Tests in ci."""

import subprocess

from common import run_with_exit_code


def run_pytest_quiet() -> bool:
    """Run pytest quiet."""
    result = subprocess.run(["pytest", "-q"], check=False)
    return result.returncode == 0


def main() -> int:
    """Main."""
    return run_with_exit_code(run_pytest_quiet)


if __name__ == "__main__":
    raise SystemExit(main())
