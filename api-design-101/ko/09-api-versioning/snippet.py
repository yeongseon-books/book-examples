"""Generated from book-content article."""

from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

SUNSET_DATE = "Wed, 31 Jan 2027 23:59:59 GMT"
SUNSET_DATETIME = datetime(2027, 1, 31, 23, 59, 59)

@app.get("/v1/users/{uid}")
def v1_get_user(uid: int):
    now = datetime.utcnow()

    # Sunset 이후면 410 반환
    if now > SUNSET_DATETIME:
        return JSONResponse(
            status_code=410,
            content={"code": "version.sunset", "detail": "v1은 종료되었습니다. /v2를 사용하세요."},
        )

    # 정상 응답 + deprecation header
    return JSONResponse(
        content={"id": uid, "name": "Y"},
        headers={
            "Deprecation": "true",
            "Sunset": SUNSET_DATE,
            "Link": '</v2/users>; rel="successor-version"',
        },
    )
