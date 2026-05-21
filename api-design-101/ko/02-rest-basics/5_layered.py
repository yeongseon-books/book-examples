# 5_layered.py
import requests

# 클라이언트는 이 URL 뒤에 CDN, LB, Gateway가 있는지 모름
# 계약만 맞으면 인프라 구성은 자유롭게 바꿀 수 있음
r = requests.get("https://api.myservice.com/products/1")
assert r.status_code == 200
