# 4_protected.py
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

def current_user(authorization: str = Header(...)):
    try:
        token = authorization.removeprefix("Bearer ")
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        return data["sub"]
    except Exception:
        raise HTTPException(401)

@app.get("/me")
def me(user: str = Depends(current_user)):
    return {"user": user}
