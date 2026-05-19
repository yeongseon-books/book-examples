"""Information Security 101 - Episode 7: Secret management."""

import secrets

from common import SecretsVault

vault = SecretsVault(secrets.token_bytes(32))
vault.put("api_key", "demo-secret")
vault.rotate_master_key(secrets.token_bytes(32))
print({"secret": vault.get("api_key"), "events": len(vault.audit)})
