# 1_client_server.py
import requests

# 클라이언트는 서버가 Python인지 Go인지 모름
# 오직 계약(URL + method + 응답 형태)만 알면 됨
r = requests.get("https://api.github.com")
print(r.status_code)  # 200
print(r.json().keys())  # 사용 가능한 리소스 URL 목록
