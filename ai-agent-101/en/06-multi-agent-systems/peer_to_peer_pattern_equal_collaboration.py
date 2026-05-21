"""Generated from book-content article."""

from typing import List, Optional


class PeerAgent:
    """A peer agent."""

    def __init__(self, name: str, role: str, api_key: str):
        self.name = name
        self.role = role
        self.client = OpenAI(api_key=api_key)
        self.peers: list[PeerAgent] = []
        self.message_history: list[Dict] = []

    def add_peer(self, peer: "PeerAgent") -> None:
        """Add a peer."""
        if peer not in self.peers:
            self.peers.append(peer)

    def send_message(self, recipient: "PeerAgent", message: str) -> str:
        """Send a message to a peer."""
        msg = {
            "from": self.name,
            "to": recipient.name,
            "content": message
        }
        self.message_history.append(msg)
        return recipient.receive_message(self, message)

    def receive_message(self, sender: "PeerAgent", message: str) -> str:
        """Receive a message and respond."""
        prompt = f"""You are {self.name}, a {self.role}.
Message from {sender.name}: {message}

Respond appropriately. If you need help from another peer, mention it."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        reply = response.choices[0].message.content

        self.message_history.append({
            "from": sender.name,
            "to": self.name,
            "content": message,
            "reply": reply
        })
        return reply

    def collaborate(self, task: str) -> str:
        """Collaborate with peers on a task."""
        # Find a peer that can help
        for peer in self.peers:
            if self._needs_help_from(peer, task):
                return self.send_message(peer, task)
        # Handle alone if no help is needed
        return self._handle_alone(task)

    def _needs_help_from(self, peer: "PeerAgent", task: str) -> bool:
        """Determine whether help from this peer is needed."""
        # Simplified judgment logic
        keywords = {
            "writer": ["write", "draft", "compose"],
            "reviewer": ["review", "check", "feedback"],
            "researcher": ["research", "find", "investigate"]
        }
        for role, kws in keywords.items():
            if role in peer.role.lower():
                if any(kw in task.lower() for kw in kws):
                    return True
        return False

    def _handle_alone(self, task: str) -> str:
        """Handle the task alone."""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are {self.name}, a {self.role}."},
                {"role": "user", "content": task}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

# Example usage
writer = PeerAgent("Writer", "technical writer", "your-key")
reviewer = PeerAgent("Reviewer", "content reviewer", "your-key")

# Register each other as peers
writer.add_peer(reviewer)
reviewer.add_peer(writer)

# Start collaboration
result = writer.collaborate("Write and review a blog post about REST APIs")
# Writer drafts and hands off to Reviewer
# Reviewer gives feedback and Writer revises
