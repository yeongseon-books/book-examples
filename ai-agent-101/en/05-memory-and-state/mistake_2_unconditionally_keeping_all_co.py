# Continuously accumulate even as conversation grows
class MemoryNoLimit:
    def __init__(self):
        self.messages = []
    
    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        # Token overflow or cost explosion after dozens of exchanges
