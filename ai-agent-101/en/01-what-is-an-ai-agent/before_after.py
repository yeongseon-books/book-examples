"""Generated from book-content article."""

goal = "Tell me whether I need an umbrella in Tokyo today"
agent = Agent(tools=[get_weather], llm=llm)
result = agent.run(goal)
# → "Yes, rain is forecast in Tokyo today (18°C, rain)"
