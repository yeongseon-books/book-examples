# 1_hash.py
from passlib.hash import bcrypt

hashed = bcrypt.hash("mySecret123")
print(bcrypt.verify("mySecret123", hashed))  # True
