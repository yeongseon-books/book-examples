# 2_web_api.py
import requests

r = requests.get("https://api.github.com/repos/python/cpython")
print(f"Status: {r.status_code}")
print(f"Repo: {r.json()['full_name']}")
print(f"Stars: {r.json()['stargazers_count']}")
