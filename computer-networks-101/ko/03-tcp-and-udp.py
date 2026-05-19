import socket
import threading
from typing import cast


def compare_transports(payload: bytes = b"transport-demo") -> dict[str, bytes]:
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("127.0.0.1", 0))
    tcp_server.listen(1)
    tcp_addr = cast("tuple[str, int]", tcp_server.getsockname())
    tcp_port = tcp_addr[1]

    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(("127.0.0.1", 0))
    udp_addr = cast("tuple[str, int]", udp_server.getsockname())
    udp_port = udp_addr[1]

    def serve_tcp() -> None:
        conn, _addr = cast("tuple[socket.socket, tuple[str, int]]", tcp_server.accept())
        with conn:
            data = conn.recv(4096)
            conn.sendall(data)
        tcp_server.close()

    def serve_udp() -> None:
        data, addr = cast("tuple[bytes, tuple[str, int]]", udp_server.recvfrom(4096))
        _ = udp_server.sendto(data, addr)
        udp_server.close()

    tcp_thread = threading.Thread(target=serve_tcp, daemon=True)
    udp_thread = threading.Thread(target=serve_udp, daemon=True)
    tcp_thread.start()
    udp_thread.start()

    with socket.create_connection(("127.0.0.1", tcp_port), timeout=1.5) as tcp_client:
        _ = tcp_client.sendall(payload)
        tcp_echo = tcp_client.recv(4096)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
        udp_client.settimeout(1.5)
        _ = udp_client.sendto(payload, ("127.0.0.1", udp_port))
        udp_echo, _remote = cast(
            "tuple[bytes, tuple[str, int]]", udp_client.recvfrom(4096)
        )

    tcp_thread.join(timeout=1.0)
    udp_thread.join(timeout=1.0)
    return {"tcp": tcp_echo, "udp": udp_echo}


if __name__ == "__main__":
    print(compare_transports())
