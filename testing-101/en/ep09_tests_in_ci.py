import subprocess

from common import run_with_exit_code


def run_pytest_quiet() -> bool:
    result = subprocess.run(["pytest", "-q"], check=False)
    return result.returncode == 0


def main() -> int:
    return run_with_exit_code(run_pytest_quiet)


if __name__ == "__main__":
    raise SystemExit(main())
