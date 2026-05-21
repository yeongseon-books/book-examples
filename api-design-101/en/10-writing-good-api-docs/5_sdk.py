# 5_sdk.py
from example_api import Client

c = Client(api_key="...")
print(c.users.get(42))
