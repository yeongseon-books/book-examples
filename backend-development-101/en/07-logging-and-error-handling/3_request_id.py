# 3_request_id.py
import logging
import uuid

from fastapi import FastAPI, Request

app = FastAPI()
log = logging.getLogger("app")

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    rid = str(uuid.uuid4())
    request.state.rid = rid
    response = await call_next(request)
    response.headers["X-Request-ID"] = rid
    log.info(f"req rid={rid} path={request.url.path}")
    return response
