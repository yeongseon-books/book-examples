"""Computer Networks 101 - Episode 5: Http and https."""

import http.client
import http.server
import json
import socketserver
import threading
from typing import cast


def parse_http_request(raw: str) -> dict[str, object]:
    """Parse http request."""
    head, body = raw.split("\r\n\r\n", 1)
    lines = head.split("\r\n")
    method, path, version = lines[0].split(" ")
    headers = {}
    for line in lines[1:]:
        key, value = line.split(":", 1)
        headers[key.strip().lower()] = value.strip()
    return {
        "method": method,
        "path": path,
        "version": version,
        "headers": headers,
        "body": body,
    }


def build_http_response(
    status: int, body: str, content_type: str = "text/plain"
) -> bytes:
    """Build http response."""
    payload = body.encode()
    lines = [
        f"HTTP/1.1 {status} OK",
        f"Content-Type: {content_type}",
        f"Content-Length: {len(payload)}",
        "Connection: close",
        "",
        "",
    ]
    return "\r\n".join(lines).encode() + payload


class DemoHandler(http.server.BaseHTTPRequestHandler):
    """Demo handler."""

    def do_GET(self) -> None:
        """Do  g e t."""
        payload = json.dumps({"path": self.path, "secure": False}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        _ = self.wfile.write(payload)


def run_local_http_demo() -> dict[str, object]:
    """Run local http demo."""
    with socketserver.TCPServer(("127.0.0.1", 0), DemoHandler) as server:
        port = server.server_address[1]
        thread = threading.Thread(target=server.handle_request, daemon=True)
        thread.start()
        conn = http.client.HTTPConnection("127.0.0.1", int(port), timeout=2)
        conn.request("GET", "/health")
        response = conn.getresponse()
        data = cast("dict[str, object]", json.loads(response.read().decode()))
        conn.close()
        thread.join(timeout=1.0)
        return {"status": response.status, "path": data["path"]}


if __name__ == "__main__":
    print(run_local_http_demo())
