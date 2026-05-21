# 4_global_handler.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class DomainError(Exception):
    def __init__(self, code: str, message: str):
        self.code, self.message = code, message

@app.exception_handler(DomainError)
async def handle_domain(_: Request, exc: DomainError):
    return JSONResponse(
        status_code=400,
        content={"code": exc.code, "message": exc.message},
    )
