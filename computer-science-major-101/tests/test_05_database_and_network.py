import socket
import threading
from collections.abc import Callable

from conftest import load_module


def test_tcp_kv_store_set_get() -> None:
    mod = load_module("ko/05-database-and-network.py")
    start_kv_server: Callable[
        [str, int], tuple[socket.socket, int, dict[str, str], threading.Thread]
    ] = mod.start_kv_server
    kv_client_request: Callable[[str, int, str], str] = mod.kv_client_request

    server, port, _, _ = start_kv_server("127.0.0.1", 0)
    try:
        assert kv_client_request("127.0.0.1", port, "SET major cs") == "OK"
        assert kv_client_request("127.0.0.1", port, "GET major") == "cs"
        assert kv_client_request("127.0.0.1", port, "GET missing") == "NULL"
    finally:
        server.close()
