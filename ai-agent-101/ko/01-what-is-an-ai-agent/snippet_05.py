"""Generated from book-content article."""

goal = "Tell me whether I need an umbrella in Tokyo today"

# observe
context = {"goal": goal, "history": []}

# think (you decide)
next_action = ("get_weather", {"city": "Tokyo"})

# act
result = get_weather(**next_action[1])
context["history"].append((next_action, result))

# check
print(context)
# {'goal': '...', 'history': [(('get_weather', {'city': 'Tokyo'}),
#                              {'temp': 18, 'condition': 'rain'})]}
