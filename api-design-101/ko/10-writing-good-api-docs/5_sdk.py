# Python SDK 예시
from example_api import Client

client = Client(api_key="sk_test_abc123")
customer = client.customers.create(name="Alice", email="alice@example.com")
print(customer.id)  # cus_abc
