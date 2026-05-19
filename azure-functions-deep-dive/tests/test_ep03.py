from conftest import load_module

ko_run = load_module("ko/03-grpc-event-stream/step01_grpc_stream.py", "ko_ep03").run
en_run = load_module("en/03-grpc-event-stream/step01_grpc_stream.py", "en_ep03").run


def test_ep03_capability_negotiation() -> None:
    ko_result = ko_run()
    en_result = en_run()
    assert ko_result["start_stream"]["worker_id"] == "worker-42"
    assert en_result["negotiated_capabilities"] == ["SharedMemoryDataTransfer"]
