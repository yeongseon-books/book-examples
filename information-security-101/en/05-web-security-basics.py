from common import WebRequestSanitizer

s = WebRequestSanitizer()
headers = {"Host": "api.example.com", "X-CSRF": "csrf-2"}
print(
    {
        "headers_ok": s.validate_headers(headers),
        "cors_ok": s.cors_allows(
            "https://app.example.com", {"https://app.example.com"}
        ),
    }
)
