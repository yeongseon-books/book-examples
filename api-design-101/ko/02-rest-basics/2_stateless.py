# Stateless: 매 요청에 인증 정보를 포함
# GET /users/42
# Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

# 위 HTTP 요청 예시는 매 요청마다 인증 토큰을 포함하는 무상태 설계를 보여줍니다.
# 서버는 세션 상태를 저장하지 않으므로, 클라이언트가 매번 필요한 정보를 모두 전달합니다.
print("Stateless 설계: 매 요청에 Authorization 헤더를 포함합니다.")
print("GET /users/42")
print("Authorization: Bearer eyJhbGciOiJIUzI1NiIs...")
