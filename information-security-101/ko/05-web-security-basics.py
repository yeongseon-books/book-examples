from common import WebRequestSanitizer

s = WebRequestSanitizer()
headers = {"Host": "app.example.com", "X-CSRF": "csrf-1"}
print(
    {
        "headers_ok": s.validate_headers(headers),
        "csrf_ok": s.check_csrf(headers, "csrf-1"),
    }
)
