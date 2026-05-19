import os

import pytest

from ko import _04_environments_and_config as ep04


def test_missing_required_key_and_redaction(tmp_path) -> None:
    env_file = tmp_path / 'app.env'
    env_file.write_text('API_URL=http://localhost\nPASSWORD=secret\nTOKEN=abc\n', encoding='utf-8')
    os.environ.pop('DB_URL', None)
    with pytest.raises(KeyError):
        ep04.load_config('dev', ['API_URL', 'DB_URL'], str(env_file))
    config = ep04.load_config('dev', ['API_URL'], str(env_file))
    redacted = ep04.redact_secrets(config)
    assert redacted['PASSWORD'] == '***REDACTED***'
    assert redacted['TOKEN'] == '***REDACTED***'
