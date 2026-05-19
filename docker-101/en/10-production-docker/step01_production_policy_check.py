from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import SecurityPolicyChecker

# English note: offline validation example.


def run() -> dict[str, object]:
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
