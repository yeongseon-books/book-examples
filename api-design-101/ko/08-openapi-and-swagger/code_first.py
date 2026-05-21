"""Generated from book-content article."""

from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"

class Order(BaseModel):
    id: str
    status: OrderStatus
    created_at: str

app = FastAPI(title="Order API", version="1.0")

@app.get("/orders", response_model=list[Order])
def list_orders(status: OrderStatus | None = Query(None)):
    """주문 목록을 조회합니다."""
    ...
