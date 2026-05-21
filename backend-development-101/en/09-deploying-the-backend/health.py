# health.py
@app.get("/healthz")
def healthz():
    return {"status": "ok"}
