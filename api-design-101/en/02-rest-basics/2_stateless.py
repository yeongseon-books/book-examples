# 2_stateless.py
import requests
# Every call is *self-contained* — credentials travel each time
headers = {"Authorization": "token TEST"}
requests.get("https://api.example.com/me", headers=headers)
