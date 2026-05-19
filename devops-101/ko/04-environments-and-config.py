from __future__ import annotations

import os
from pathlib import Path


def parse_env_file(path: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def load_config(
    environment: str, required_keys: list[str], env_file: str | None = None
) -> dict[str, str]:
    config = parse_env_file(env_file) if env_file else {}
    config.update({k: v for k, v in os.environ.items()})
    config["ENVIRONMENT"] = environment

    missing = [key for key in required_keys if not config.get(key)]
    if missing:
        raise KeyError(f"Missing required config keys: {', '.join(missing)}")

    return config


def redact_secrets(values: dict[str, str]) -> dict[str, str]:
    redacted = {}
    for key, value in values.items():
        if "PASSWORD" in key or "TOKEN" in key or "SECRET" in key:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value
    return redacted
