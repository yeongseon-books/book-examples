"""Generated from book-content article."""

from typing import List, Optional


class HierarchicalAgent:
    """A hierarchical agent."""

    def __init__(self, name: str, role: str, level: int, api_key: str):
        self.name = name
        self.role = role
        self.level = level  # 0 = top, increases downward
        self.client = OpenAI(api_key=api_key)
        self.parent: HierarchicalAgent | None = None
        self.children: list[HierarchicalAgent] = []

    def add_child(self, child: "HierarchicalAgent") -> None:
        """Add a child agent."""
        child.parent = self
        self.children.append(child)

    def execute(self, task: str) -> str:
        """Execute a task."""
        if not self.children:
            # Leaf node: execute directly
            return self._do_work(task)

        # Internal node: split and delegate to children
        subtasks = self._split_task(task)
        results = []
        for child, subtask in zip(self.children, subtasks, strict=False):
            result = child.execute(subtask)
            results.append(result)

        # Aggregate results
        return self._aggregate_results(task, results)

    def _split_task(self, task: str) -> list[str]:
        """Split the task into subtasks for each child."""
        children_info = "\n".join([
            f"- {child.name}: {child.role}"
            for child in self.children
        ])
        prompt = f"""Split the following task into subtasks for each child agent.

Task: {task}

Child agents:
{children_info}

Respond with one subtask per line, in the same order as the child agents."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        lines = response.choices[0].message.content.strip().split("\n")
        # Pad with empty strings if fewer lines than children
        while len(lines) < len(self.children):
            lines.append("")
        return lines[:len(self.children)]

    def _do_work(self, task: str) -> str:
        """Execute the task directly (leaf nodes)."""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are {self.name}, a {self.role}."},
                {"role": "user", "content": task}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    def _aggregate_results(self, task: str, results: list[str]) -> str:
        """Aggregate child results."""
        results_text = "\n\n".join([
            f"Result {i+1}: {r}" for i, r in enumerate(results)
        ])
        prompt = f"""Original task: {task}

Subtask results:
{results_text}

Synthesize the results into a coherent final answer."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content

# Example usage
# Top Manager
ceo = HierarchicalAgent("CEO", "executive director", 0, "your-key")

# Mid-level Managers
eng_manager = HierarchicalAgent("EngManager", "engineering manager", 1, "your-key")
product_manager = HierarchicalAgent("ProductManager", "product manager", 1, "your-key")

# Workers
backend_dev = HierarchicalAgent("BackendDev", "backend developer", 2, "your-key")
frontend_dev = HierarchicalAgent("FrontendDev", "frontend developer", 2, "your-key")
designer = HierarchicalAgent("Designer", "ux designer", 2, "your-key")

# Build the hierarchy
ceo.add_child(eng_manager)
ceo.add_child(product_manager)
eng_manager.add_child(backend_dev)
eng_manager.add_child(frontend_dev)
product_manager.add_child(designer)

# Run a task
result = ceo.execute("Plan a new user dashboard feature")
