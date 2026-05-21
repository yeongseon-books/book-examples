"""Generated from book-content article."""

class Agent:
    def __init__(self, user_id):
        self.user_id = user_id
        # Load once on session start
        self.preferences = long_term_memory.retrieve(user_id)

    def run(self, user_message):
        # Use already-loaded preferences
        context = build_context(self.preferences, user_message)
        response = llm.generate(context)
        return response
