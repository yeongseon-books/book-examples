# 3_verify.py
import jwt

data = jwt.decode(token, SECRET, algorithms=["HS256"])
print(data["sub"])
