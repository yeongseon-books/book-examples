# server.py
@app.post("/login")
def login(body):
    if not auth.verify(body["email"], body["password"]):
        return 401, {"error": "invalid"}
    return 200, {"token": auth.token(body["email"])}
