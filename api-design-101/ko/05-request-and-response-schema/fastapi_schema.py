# fastapi_schema.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()


class UserCreate(BaseModel):  # 입력 schema
    username: str = Field(min_length=3, max_length=32)
    email: str


class UserResponse(BaseModel):  # 출력 schema
    id: int
    username: str
    created_at: datetime


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(body: UserCreate):
    # FastAPI가 자동으로:
    # 1) request body를 UserCreate로 검증
    # 2) 실패 시 422 + 상세 에러 반환
    # 3) 응답을 UserResponse로 직렬화
    ...
