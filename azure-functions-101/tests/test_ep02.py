from conftest import run_script


def test_ep02() -> None:
    output = run_script("ko/02-triggers-and-bindings/step01_queue_to_invoice.py")
    assert "'amount': 35000" in output
