import datetime

from en import ep07_system_sensitive


def test_ep07_tmp_path_and_setenv(monkeypatch, tmp_path):
    class FixedDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2026, 1, 15)

    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setattr(ep07_system_sensitive.datetime, "date", FixedDate)

    path = ep07_system_sensitive.write_daily_note(tmp_path, "hello")
    assert path.name == "test-2026-01-15.txt"
    assert path.read_text(encoding="utf-8") == "hello"
