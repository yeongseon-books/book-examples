# 5_call.py
import requests

# /health 계약 검증
r = requests.get("http://localhost:8000/health")
assert r.status_code == 200
assert r.json() == {"status": "ok"}

# /users 계약 검증
r = requests.get("http://localhost:8000/users")
assert r.status_code == 200
assert isinstance(r.json(), list)
assert "name" in r.json()[0]

print("All contracts verified.")
