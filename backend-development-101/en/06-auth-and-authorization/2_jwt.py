# 2_jwt.py
import time

import jwt

SECRET = "change-me"
token = jwt.encode({"sub": "alice", "exp": time.time() + 3600}, SECRET, algorithm="HS256")
print(token)
