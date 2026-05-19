"""Azure App Service 101 - Episode 1: Configuration patterns."""

from __future__ import annotations

import os


def require_env(name: str) -> str:
    """Require env."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def key_vault_reference(vault_name: str, secret_name: str) -> str:
    """Key vault reference."""
    return (
        "@Microsoft.KeyVault(SecretUri=https://"
        f"{vault_name}.vault.azure.net/secrets/{secret_name}/)"
    )


def classify_setting(name: str) -> str:
    """Classify setting."""
    sensitive = {"DB_PASSWORD", "PAYMENTS_API_KEY", "DATABASE_URL"}
    return "key_vault" if name in sensitive else "app_settings"
