from pathlib import Path

from en.ep08_file_io_exceptions import parse_csv_like, write_and_read_demo


def test_parse_csv_like() -> None:
    assert parse_csv_like("a,1\nb,2") == [("a", 1), ("b", 2)]


def test_write_and_read_demo(tmp_path: Path) -> None:
    path = tmp_path / "sample.txt"
    assert write_and_read_demo(path, "hello") == "hello"
