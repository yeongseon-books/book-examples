"""Generated from book-content article."""

from typing import List, Dict
from openai import OpenAI

class WorkerAgent:
    """A specialized worker agent."""

    def __init__(self, name: str, role: str, api_key: str):
        self.name = name
        self.role = role
        self.client = OpenAI(api_key=api_key)

    def execute(self, task: str) -> str:
        """Execute a task."""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a {self.role}."},
                {"role": "user", "content": task}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

class OrchestratorAgent:
    """An orchestrator agent that coordinates workers."""

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.workers: Dict[str, WorkerAgent] = {}

    def register_worker(self, worker: WorkerAgent) -> None:
        """Register a worker."""
        self.workers[worker.name] = worker

    def plan(self, request: str) -> List[Dict]:
        """Decompose the request into subtasks."""
        worker_list = "\n".join([
            f"- {name}: {w.role}"
            for name, w in self.workers.items()
        ])
        prompt = f"""Break down the following request into subtasks and assign each to the appropriate worker.

Available workers:
{worker_list}

Request: {request}

Respond in JSON format:
[
  {{"worker": "worker_name", "task": "task description"}},
  ...
]
"""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        import json
        return json.loads(response.choices[0].message.content)

    def handle(self, request: str) -> Dict:
        """Handle the request."""
        subtasks = self.plan(request)
        results = {}
        for subtask in subtasks:
            worker_name = subtask["worker"]
            task = subtask["task"]
            if worker_name in self.workers:
                results[worker_name] = self.workers[worker_name].execute(task)
        return results

# Example usage
orchestrator = OrchestratorAgent(api_key="your-key")

# Register workers
researcher = WorkerAgent("researcher", "research analyst", "your-key")
writer = WorkerAgent("writer", "technical writer", "your-key")
reviewer = WorkerAgent("reviewer", "content reviewer", "your-key")

orchestrator.register_worker(researcher)
orchestrator.register_worker(writer)
orchestrator.register_worker(reviewer)

# Handle a request
result = orchestrator.handle("Write a blog post about Python async programming")
