import socket
import threading
from typing import cast


def _handle_client(conn: socket.socket, store: dict[str, str]) -> None:
    with conn:
        conn.settimeout(1.0)
        while True:
            data = conn.recv(4096)
            if not data:
                return
            line = data.decode("utf-8").strip()
            parts = line.split(" ", 2)
            cmd = parts[0].upper()
            if cmd == "SET" and len(parts) == 3:
                key, value = parts[1], parts[2]
                store[key] = value
                conn.sendall(b"OK\n")
            elif cmd == "GET" and len(parts) == 2:
                value = store.get(parts[1])
                conn.sendall(
                    ("NULL\n" if value is None else f"{value}\n").encode("utf-8")
                )
            else:
                conn.sendall(b"ERR\n")


def start_kv_server(
    host: str = "127.0.0.1", port: int = 0
) -> tuple[socket.socket, int, dict[str, str], threading.Thread]:
    store: dict[str, str] = {}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    sockname = cast("tuple[str, int]", server.getsockname())
    bound_port = sockname[1]

    def _serve() -> None:
        while True:
            try:
                conn, _addr = cast(
                    "tuple[socket.socket, tuple[str, int]]", server.accept()
                )
            except OSError:
                return
            _handle_client(conn, store)

    thread = threading.Thread(target=_serve, daemon=True)
    thread.start()
    return server, bound_port, store, thread


def kv_client_request(host: str, port: int, command: str) -> str:
    with socket.create_connection((host, port), timeout=1.0) as client:
        client.sendall((command + "\n").encode("utf-8"))
        return client.recv(4096).decode("utf-8").strip()


if __name__ == "__main__":
    server, port, _, _ = start_kv_server()
    try:
        print(kv_client_request("127.0.0.1", port, "SET major cs"))
        print(kv_client_request("127.0.0.1", port, "GET major"))
    finally:
        server.close()
