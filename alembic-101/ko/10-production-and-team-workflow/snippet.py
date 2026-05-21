"""Generated from book-content article."""

@app.get("/health")
def health():
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version_num FROM alembic_version")).scalar()
    return {"status": "ok", "alembic_version": version, "expected": EXPECTED_VERSION}
