# 2_fastapi.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "hello"
