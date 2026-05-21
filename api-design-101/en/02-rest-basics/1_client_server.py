# 1_client_server.py
# Client owns the UI; server owns the data — either side must be replaceable
import requests
print(requests.get("https://api.github.com").status_code)
