from __future__ import annotations

from conftest import load_module


def test_ep01_ls_lists_created_file() -> None:
    run = load_module("ko/01-what-is-cli-and-shell/step01_cli_shell.py", "ep01").run
    out = run()
    assert out["code"] == 0
    assert "a.txt" in str(out["stdout"])


def test_ep02_file_directory_ops() -> None:
    run = load_module("ko/02-files-and-directories/step01_files_dirs.py", "ep02").run
    out = run()
    assert out["code"] == 0
    assert "copy.txt" in str(out["stdout"])


def test_ep03_chmod_600_mode() -> None:
    run = load_module(
        "ko/03-permissions-and-ownership/step01_permissions.py", "ep03"
    ).run
    out = run()
    assert out["mode"] == "0o600"


def test_ep04_head_reads_first_lines() -> None:
    run = load_module("ko/04-viewing-files/step01_viewing.py", "ep04").run
    out = run()
    assert out["code"] == 0
    assert str(out["stdout"]).splitlines() == ["line1", "line2"]


def test_ep05_grep_finds_pattern() -> None:
    run = load_module("ko/05-grep-find-xargs/step01_search_trio.py", "ep05").run
    out = run()
    assert out["code"] == 0
    assert "TODO" in str(out["stdout"])


def test_ep06_pipe_filters_error() -> None:
    run = load_module("ko/06-pipe-and-redirection/step01_pipe_redirect.py", "ep06").run
    out = run()
    assert out["code"] == 0
    assert "error" in str(out["stdout"])


def test_ep07_process_spawn_and_terminate() -> None:
    run = load_module("ko/07-process-management/step01_process.py", "ep07").run
    out = run()
    assert out["running_before"] is True
    assert out["running_after"] is False


def test_ep08_env_scope_restore() -> None:
    run = load_module("ko/08-environment-variables/step01_env.py", "ep08").run
    out = run()
    assert out["inside"] == "linux-cli-101"
    assert out["restored"] == out["original"]


def test_ep09_shell_script_exit_zero() -> None:
    run = load_module("ko/09-shell-script-basics/step01_script.py", "ep09").run
    out = run()
    assert out["code"] == 0
    assert "hello script" in str(out["stdout"])


def test_ep10_ssh_sim_records_commands() -> None:
    run = load_module("ko/10-ssh-and-remote/step01_ssh_sim.py", "ep10").run
    out = run()
    assert out["ok"]["code"] == 0
    assert out["fail"]["code"] == 255
    assert out["commands"] == [("deploy", "ls /opt/app")]
