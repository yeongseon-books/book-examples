# Bad example
# Each agent passes free-form messages
agent_a.send("Hey, can you check this?")
agent_b.send({"task": "review", "content": "..."})
agent_c.send("REVIEW_NEEDED:doc123")
# Inconsistent formats make tracking and debugging hard

# Good example
# Use a standard message format
message = Message(
    sender="AgentA",
    receiver="AgentB",
    message_type=MessageType.REQUEST,
    content={"action": "review", "data": "doc123"}
)
broker.send(message)
