from __future__ import annotations


def resolve_mounts(spec: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for mount in spec:
        target = mount["target"]
        if target in seen:
            raise ValueError(f"duplicate mount target: {target}")
        seen.add(target)
        out.append(mount)
    return out


def detect_overlap(spec: list[dict[str, str]]) -> list[tuple[str, str]]:
    targets = [m["target"].rstrip("/") for m in spec]
    conflicts: list[tuple[str, str]] = []
    for i, left in enumerate(targets):
        for right in targets[i + 1 :]:
            if right.startswith(left + "/") or left.startswith(right + "/"):
                conflicts.append((left, right))
    return conflicts
