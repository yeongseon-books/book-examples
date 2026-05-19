"""Cloud Computing 101 - Episode 1: Iam policy."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def build_iam_policy(bucket: str) -> dict[str, object]:
    """Build iam policy."""
    statement = {
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": [f"arn:aws:s3:::{bucket}/*"],
    }
    return record("iam", "create_policy", version="2012-10-17", statements=[statement])
