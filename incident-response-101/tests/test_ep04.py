from conftest import load_module

run = load_module("ko/04-communication/step01_example.py", "ep04").run

def test_ep04_customer_message_prefix() -> None:
    result = run()
    assert result["customer"].startswith("Customer Update:")
