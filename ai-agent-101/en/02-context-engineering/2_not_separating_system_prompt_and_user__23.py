# Good example
messages = [
    {"role": "system", "content": "You are an agent that only queries the DB. Never execute DELETE/UPDATE."},
    {"role": "user", "content": user_input}  # Separated and safe
]
