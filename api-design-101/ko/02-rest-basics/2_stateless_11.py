# 2_stateless.py
import requests

# 매 요청에 인증 정보를 포함 — 서버는 이전 요청을 기억하지 않음
headers = {"Authorization": "Bearer my-token-123"}

# 이 두 요청은 서로 독립적 — 어느 서버 인스턴스가 받아도 동일 결과
r1 = requests.get("https://api.example.com/users/1", headers=headers)
r2 = requests.get("https://api.example.com/users/2", headers=headers)
