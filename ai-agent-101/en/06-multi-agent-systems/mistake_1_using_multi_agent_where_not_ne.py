# Bad example
# Using 3 agents for a simple document summary
agent1 = Agent("Reader")     # Reads the doc
agent2 = Agent("Summarizer") # Summarizes
agent3 = Agent("Formatter")  # Formats output
# Overengineered: a single agent is sufficient

# Good example
# A single agent handles it
agent = Agent("DocProcessor")
result = agent.process_document(doc)
