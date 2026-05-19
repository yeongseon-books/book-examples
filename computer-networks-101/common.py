from __future__ import annotations

import json
import socket
import threading
from collections.abc import Callable


def start_tcp_echo_server() -> tuple[threading.Thread, int]:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]

    def run() -> None:
        conn, _ = server.accept()
        with conn:
            data = conn.recv(4096)
            if data:
                conn.sendall(data)
        server.close()

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread, int(port)


def start_udp_echo_server() -> tuple[threading.Thread, int]:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 0))
    port = server.getsockname()[1]

    def run() -> None:
        data, addr = server.recvfrom(4096)
        server.sendto(data, addr)
        server.close()

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread, int(port)


def run_tcp_client(message: bytes, port: int) -> bytes:
    with socket.create_connection(("127.0.0.1", port), timeout=1.5) as client:
        client.sendall(message)
        return client.recv(4096)


def run_udp_client(message: bytes, port: int) -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(1.5)
        client.sendto(message, ("127.0.0.1", port))
        data, _ = client.recvfrom(4096)
        return data


def parse_json_lines(raw: str) -> list[dict[str, object]]:
    return [json.loads(line) for line in raw.splitlines() if line.strip()]


def retry_until(timeout_seconds: float, action: Callable[[], bool]) -> bool:
    deadline = timeout_seconds
    while deadline > 0:
        if action():
            return True
        deadline -= 0.01
    return False
