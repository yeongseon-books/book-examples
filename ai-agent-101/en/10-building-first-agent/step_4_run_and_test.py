"""Generated from book-content article."""

if __name__ == "__main__":
    agent = ResearchAgent()
    print("Research Assistant. Type 'quit' to exit.")
    while True:
        user_input = input("\nQuestion: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            break
        if not user_input:
            continue
        try:
            answer = agent.run(user_input)
            print(f"\nAnswer: {answer}")
        except Exception as exc:
            print(f"\n[error] {exc}")
