"""Generated from book-content article."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a research assistant.
Use the search and calculator tools to answer user questions.
Synthesize tool results into accurate, concise answers.
Say you do not know when you do not."""

class ResearchAgent:
    """Research assistant agent."""

    def __init__(self, model: str = "gpt-4o-mini", max_iterations: int = 5):
        self.model = model
        self.max_iterations = max_iterations
        self.memory = ConversationMemory(SYSTEM_PROMPT)

    def run(self, user_input: str) -> str:
        """Process a user question and return an answer."""
        self.memory.add("user", user_input)

        for _iteration in range(self.max_iterations):
            response = client.chat.completions.create(
                model=self.model,
                messages=self.memory.to_openai(),
                tools=tools_to_openai_format(),
                tool_choice="auto",
            )
            msg = response.choices[0].message

            if not msg.tool_calls:
                self.memory.add("assistant", msg.content or "")
                return msg.content or ""

            self.memory.add(
                "assistant",
                msg.content or "",
                tool_calls=[tc.model_dump() for tc in msg.tool_calls],
            )

            for tool_call in msg.tool_calls:
                result = self._execute_tool(tool_call)
                self.memory.add(
                    "tool",
                    json.dumps(result, ensure_ascii=False),
                    tool_call_id=tool_call.id,
                )

        return "Max iterations reached without producing an answer."

    def _execute_tool(self, tool_call: Any) -> Any:
        """Execute a tool safely."""
        name = tool_call.function.name
        try:
            args = json.loads(tool_call.function.arguments)
            tool = TOOLS.get(name)
            if not tool:
                return {"error": f"Unknown tool: {name}"}
            validated = tool["schema"](**args)
            result = tool["function"](**validated.model_dump())
            return {"result": result}
        except Exception as exc:
            return {"error": str(exc)}
