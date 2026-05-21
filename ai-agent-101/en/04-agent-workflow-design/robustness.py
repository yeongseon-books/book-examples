"""Generated from book-content article."""

def robust_workflow(tasks: List[str]) -> Dict[str, Any]:
    """Robust workflow: continue despite partial failures"""
    
    results = {
        "successful": [],
        "failed": []
    }
    
    for task in tasks:
        try:
            result = execute_task(task)
            results["successful"].append({
                "task": task,
                "result": result
            })
        except Exception as e:
            # Continue despite failure
            results["failed"].append({
                "task": task,
                "error": str(e)
            })
            log_error(task, e)
    
    # Partial success is still valuable
    return results
