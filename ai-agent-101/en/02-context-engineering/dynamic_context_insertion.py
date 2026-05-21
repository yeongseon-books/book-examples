"""Generated from book-content article."""

def build_dynamic_context(user_query: str, user_id: str) -> str:
    """Builds user-specific context."""
    # Retrieve user information
    user = get_user_profile(user_id)
    recent_orders = get_recent_orders(user_id, limit=3)
    
    context = f"""
User information:
- Name: {user['name']}
- Tier: {user['tier']} (Joined: {user['joined_date']})
- Recent orders: {', '.join([o['product'] for o in recent_orders])}

Current time: {datetime.now().strftime('%Y-%m-%d %H:%M')}

User query: {user_query}
"""
    return context

# Pass dynamic context when calling agent
response = agent.run(
    system_prompt=base_system_prompt,
    context=build_dynamic_context(query, user_id)
)
