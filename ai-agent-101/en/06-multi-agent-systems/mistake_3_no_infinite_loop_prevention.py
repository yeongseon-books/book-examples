# Bad example
# AgentA and AgentB keep sending messages to each other
# AgentA: "I need help" → AgentB
# AgentB: "I need more info" → AgentA
# AgentA: "What info?" → AgentB
# AgentB: "I don't know" → AgentA
# Infinite loop

# Good example
# Limit max iterations and message depth
class LoopProtectedAgent:
    MAX_DEPTH = 5

    def communicate(self, message, depth=0):
        if depth >= self.MAX_DEPTH:
            return "Max depth reached. Terminating."
        # ... handle message ...
