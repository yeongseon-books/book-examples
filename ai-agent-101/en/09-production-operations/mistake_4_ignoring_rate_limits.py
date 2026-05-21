# Bad
for _item in items:  # 10,000 items
    response = openai.ChatCompletion.create(...)  # exceeds API quota

# Good
limiter = RateLimiter(60, 60)
for _item in items:
    limiter.wait_and_acquire()
    response = openai.ChatCompletion.create(...)
