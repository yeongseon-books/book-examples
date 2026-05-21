# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("")
def list_users():
    return []

# main.py
from fastapi import FastAPI
from routers import orders, users

app = FastAPI()
app.include_router(users.router)
app.include_router(orders.router)
