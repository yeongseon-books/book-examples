from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conftest import load_module


def test_configuration_patterns() -> None:
    mod = load_module("ko/05-configuration/step01_configuration_patterns.py", "ep05")
    require_env = cast(Any, mod.require_env)
    key_vault_reference = cast(Any, mod.key_vault_reference)
    classify_setting = cast(Any, mod.classify_setting)
    os.environ["REQUIRED_VALUE"] = "ok"
    assert require_env("REQUIRED_VALUE") == "ok"
    assert "@Microsoft.KeyVault" in key_vault_reference("vaultx", "DbPassword")
    assert classify_setting("DB_PASSWORD") == "key_vault"
    with pytest.raises(RuntimeError):
        require_env("MISSING_REQUIRED_VALUE")
