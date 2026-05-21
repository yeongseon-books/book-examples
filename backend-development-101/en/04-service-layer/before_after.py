"""Generated from book-content article."""

@app.post("/orders")
def create_order(payload, db, mail):
    if payload.amount <= 0:
        raise HTTPException(400)
    order = db.insert("orders", payload.dict())
    mail.send(payload.email, "ordered")
    return order
