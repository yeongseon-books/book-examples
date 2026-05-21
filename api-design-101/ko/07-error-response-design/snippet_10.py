"""Generated from book-content article."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid

app = FastAPI()

@app.middleware("http")
async def trace_middleware(request: Request, call_next):
    trace_id = request.headers.get("X-Trace-Id") or uuid.uuid4().hex
    request.state.trace_id = trace_id
    response = await call_next(request)
    response.headers["X-Trace-Id"] = trace_id
    return response

@app.exception_handler(Exception)
async def global_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "type": "about:blank",
            "title": "Internal server error",
            "status": 500,
            "code": "internal_error",
            "detail": "예기치 않은 오류가 발생했습니다.",
            "trace_id": request.state.trace_id,
        },
        headers={"X-Trace-Id": request.state.trace_id},
    )
