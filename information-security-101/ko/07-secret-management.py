"""Information Security 101 - Episode 7: Secret management."""

import secrets

from common import SecretsVault

vault = SecretsVault(secrets.token_bytes(32))
vault.put("db_password", "demo-secret")
print({"secret": vault.get("db_password"), "audit": vault.audit})
