# Good example
context = f"""
User: {user.name} ({user.tier})
Last 3 orders related to current query:
{format_recent_orders(orders[:3])}  # Only what's needed
"""
