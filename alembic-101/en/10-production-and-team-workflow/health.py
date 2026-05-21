# health.py
EXPECTED_VERSION = os.environ["EXPECTED_ALEMBIC_VERSION"]

@app.get("/health")
def health():
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version_num FROM alembic_version")).scalar()
    ok = version == EXPECTED_VERSION
    return {"status": "ok" if ok else "drift", "alembic_version": version, "expected": EXPECTED_VERSION}
