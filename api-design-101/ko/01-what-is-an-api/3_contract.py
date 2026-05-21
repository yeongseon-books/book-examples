# 3_contract.py
# GitHub REST API 문서에서 발췌
# GET /repos/{owner}/{repo}
#
# 경로 매개변수:
#   owner (string, required) — 저장소 소유자
#   repo  (string, required) — 저장소 이름
#
# 성공 응답: 200 OK
#   body: { "full_name": str, "stargazers_count": int, ... }
#
# 실패 응답: 404 Not Found
#   body: { "message": "Not Found" }
