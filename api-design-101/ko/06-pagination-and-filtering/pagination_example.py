# pagination_example.py
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import base64, json

app = FastAPI()

# 예시 데이터 (실제로는 DB 쿼리)
ORDERS = [
    {"id": f"ord_{i:04d}", "status": "paid", "created_at": f"2026-05-{20-i//100:02d}T{10+i%24:02d}:00:00Z"}
    for i in range(500)
]

class PaginatedResponse(BaseModel):
    data: list[dict]
    meta: dict

def encode_cursor(item: dict) -> str:
    payload = {"created_at": item["created_at"], "id": item["id"]}
    return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

def decode_cursor(token: str) -> dict:
    try:
        return json.loads(base64.urlsafe_b64decode(token.encode()).decode())
    except Exception:
        raise HTTPException(status_code=400, detail="잘못된 cursor입니다.")

@app.get("/orders", response_model=PaginatedResponse)
def list_orders(
    status: str | None = None,
    sort: str = "created_at:desc",
    limit: int = Query(default=20, le=100, ge=1),
    cursor: str | None = None,
):
    # 1. Filter
    filtered = ORDERS
    if status:
        filtered = [o for o in filtered if o["status"] == status]

    # 2. Sort (간단 구현: created_at만 지원)
    reverse = sort.endswith(":desc")
    filtered.sort(key=lambda o: o["created_at"], reverse=reverse)

    # 3. Cursor 적용
    if cursor:
        decoded = decode_cursor(cursor)
        # created_at 기준으로 이미 지난 항목 건너뛰기
        start_idx = 0
        for i, o in enumerate(filtered):
            if o["id"] == decoded["id"]:
                start_idx = i + 1
                break
        filtered = filtered[start_idx:]

    # 4. Limit
    page = filtered[:limit]
    has_more = len(filtered) > limit

    meta = {"has_more": has_more}
    if has_more and page:
        meta["next_cursor"] = encode_cursor(page[-1])

    return PaginatedResponse(data=page, meta=meta)
