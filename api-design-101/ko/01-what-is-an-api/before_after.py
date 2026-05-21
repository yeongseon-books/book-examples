"""Generated from book-content article."""

import requests

# 계약: GET /users → 200 + JSON array of user objects
response = requests.get("https://api.example.com/users")
assert response.status_code == 200
users = response.json()
