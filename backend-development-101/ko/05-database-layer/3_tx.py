# 3_tx.py
from sqlalchemy.orm import Session
with Session(engine) as s, s.begin():
    repo = UserRepository(s)
    repo.add("Alice")
    repo.add("Bob")
# Exiting cleanly commits; an exception rolls back.
