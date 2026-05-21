"""Generated from book-content article."""

from crewai import Agent, Crew, Task

researcher = Agent(
    role="Researcher",
    goal="Gather material on the given topic",
    backstory="You are a meticulous researcher.",
    tools=[search_tool],
)

writer = Agent(
    role="Writer",
    goal="Write an answer from the gathered material",
    backstory="You are a writer who values clarity.",
)

task1 = Task(description="Research FastAPI", agent=researcher)
task2 = Task(description="Summarize the research", agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = crew.kickoff()
