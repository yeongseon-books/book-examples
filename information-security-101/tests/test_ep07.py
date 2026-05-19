import secrets

from common import SecretsVault


def test_secret_rotation_keeps_readability():
    vault = SecretsVault(secrets.token_bytes(32))
    vault.put("k", "demo-secret")
    vault.rotate_master_key(secrets.token_bytes(32))
    assert vault.get("k") == "demo-secret"
