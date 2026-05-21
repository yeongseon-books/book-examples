# Execute directly in production
workflow = create_workflow(production_steps)
result = workflow.execute(real_customer_data)  # Risky!
