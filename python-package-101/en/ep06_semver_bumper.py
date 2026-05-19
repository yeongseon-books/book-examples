"""Python Package 101 - Episode 6: Semver bumper."""

import json

from common import ep06_bump_version


def main() -> None:
    """Main."""
    result = ep06_bump_version("0.1.0", "minor", prerelease="rc.1")
    print(json.dumps({"bumped": result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
