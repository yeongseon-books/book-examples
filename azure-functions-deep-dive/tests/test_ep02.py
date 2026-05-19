from conftest import load_module

ko_run = load_module("ko/02-worker-process/step01_worker_process.py", "ko_ep02").run
en_run = load_module("en/02-worker-process/step01_worker_process.py", "en_ep02").run


def test_ep02_worker_catalog() -> None:
    ko_result = ko_run()
    en_result = en_run()
    assert ko_result["worker_count"] == 2
    assert en_result["python_entry"] == "worker.py"
