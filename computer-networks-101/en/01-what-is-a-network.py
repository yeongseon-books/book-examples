"""Computer Networks 101 - Episode 1: What is a network."""

# English mirror of the corresponding episode demo
import socket
import threading
from typing import cast


def run_demo(message: bytes = b"hello network") -> bytes:
    """Run demo."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    addr = cast("tuple[str, int]", server.getsockname())
    port = addr[1]

    def serve() -> None:
        """Serve."""
        conn, _addr = cast("tuple[socket.socket, tuple[str, int]]", server.accept())
        with conn:
            data = conn.recv(4096)
            conn.sendall(data)
        server.close()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    with socket.create_connection(("127.0.0.1", port), timeout=1.5) as client:
        client.sendall(message)
        echoed = client.recv(4096)
    thread.join(timeout=1.0)
    return echoed


if __name__ == "__main__":
    print(run_demo().decode())
