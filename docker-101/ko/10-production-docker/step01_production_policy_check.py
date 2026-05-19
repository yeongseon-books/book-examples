"""Docker 101 - Episode 1: Production policy check."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import SecurityPolicyChecker

# 한국어 주석: 오프라인 검증 예제입니다.


def run() -> dict[str, object]:
    """Run."""
    runtime_flags = [
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt=no-new-privileges",
        "--user=1000:1000",
    ]
    missing = SecurityPolicyChecker().verify_runtime_flags(runtime_flags)
    tags = ["1.4.2", "sha-abc1234"]
    has_semver = bool(tags[0].count(".") == 2)
    has_sha = tags[1].startswith("sha-")
    return {
        "success": len(missing) == 0 and has_semver and has_sha,
        "missing_flags": missing,
        "tags": tags,
    }


if __name__ == "__main__":
    print(run())
